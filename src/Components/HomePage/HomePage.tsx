
import React, { useState } from "react";
import "./HomePage.css";
import axios from "axios";

const HomePage = () => {
  type OrderStatus = { orderId: string; status: string; estimatedDelivery: string; customer: string };
  type Returns = { orderId: string; returnEligible: boolean; reason: string; instructions: string };
  type Refund = { orderId: string; refundStatus: string; amount: number; method: string };
  type Faq = { q: string; a: string };
  type Kb = { id: number; title: string; content: string };


  const [orderId, setOrderId] = useState("");
  const [orderStatus, setOrderStatus] = useState<OrderStatus | null>(null);
  const [returns, setReturns] = useState<Returns | null>(null);
  const [refund, setRefund] = useState<Refund | null>(null);
  const [faq, setFaq] = useState<Faq[]>([]);
  const [kb, setKb] = useState<Kb[]>([]);
  const [loading, setLoading] = useState("");



  // Use absolute API URL for gh-pages (no proxy)
  const apiBase = window.location.hostname === "localhost" ? "" : "https://dummy-api-url.example.com";

  const fetchOrderStatus = async () => {
    setLoading("order");
    setOrderStatus(null);
    try {
      const res = await axios.get(`${apiBase}/api/order-status?orderId=${encodeURIComponent(orderId)}`);
      setOrderStatus(res.data);
    } catch (err: any) {
      setOrderStatus(null);
      if (err?.response?.data?.error) {
        alert(err.response.data.error);
      } else {
        alert("API unavailable: This demo requires a running backend server for live data.");
      }
    } finally {
      setLoading("");
    }
  };


  const fetchReturns = async () => {
    setLoading("returns");
    setReturns(null);
    try {
      const res = await axios.get(`${apiBase}/api/returns?orderId=${encodeURIComponent(orderId)}`);
      setReturns(res.data);
    } catch (err: any) {
      setReturns(null);
      if (err?.response?.data?.error) {
        alert(err.response.data.error);
      } else {
        alert("API unavailable: This demo requires a running backend server for live data.");
      }
    } finally {
      setLoading("");
    }
  };


  const fetchRefund = async () => {
    setLoading("refund");
    setRefund(null);
    try {
      const res = await axios.get(`${apiBase}/api/refunds?orderId=${encodeURIComponent(orderId)}`);
      setRefund(res.data);
    } catch (err: any) {
      setRefund(null);
      if (err?.response?.data?.error) {
        alert(err.response.data.error);
      } else {
        alert("API unavailable: This demo requires a running backend server for live data.");
      }
    } finally {
      setLoading("");
    }
  };


  const fetchFaq = async () => {
    setLoading("faq");
    try {
      const res = await axios.get(`${apiBase}/api/faq`);
      setFaq(res.data);
    } catch {
      setFaq([]);
      alert("API unavailable: This demo requires a running backend server for live data.");
    } finally {
      setLoading("");
    }
  };


  const fetchKb = async () => {
    setLoading("kb");
    try {
      const res = await axios.get(`${apiBase}/api/kb`);
      setKb(res.data);
    } catch {
      setKb([]);
      alert("API unavailable: This demo requires a running backend server for live data.");
    } finally {
      setLoading("");
    }
  };

  return (
    <div data-testid="home-page" className="home-page">
      <h1>Welcome to ShopSmart Support</h1>
      <p>Need help? Chat with our AI agent (see livechat widget) or try these quick demos:</p>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 12, margin: "24px 0" }}>
        <input
          type="text"
          placeholder="Enter Order ID (e.g. ORD12345)"
          value={orderId}
          onChange={e => setOrderId(e.target.value)}
          style={{ padding: 8, fontSize: 16, borderRadius: 4, border: '1px solid #bbb', width: 240, marginBottom: 8 }}
        />
        <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>
          <button onClick={fetchOrderStatus} disabled={loading === "order" || !orderId}>Order Status</button>
          <button onClick={fetchReturns} disabled={loading === "returns" || !orderId}>Returns</button>
          <button onClick={fetchRefund} disabled={loading === "refund" || !orderId}>Refund</button>
          <button onClick={fetchFaq} disabled={loading === "faq"}>FAQ</button>
          <button onClick={fetchKb} disabled={loading === "kb"}>Knowledge Base</button>
        </div>
      </div>
      <div style={{ marginTop: 24 }}>
        {orderStatus && (
          <div><b>Order Status:</b> {orderStatus.status} (Order: {orderStatus.orderId})<br/>Estimated Delivery: {orderStatus.estimatedDelivery}</div>
        )}
        {returns && (
          <div><b>Returns:</b> {returns.returnEligible ? "Eligible" : "Not eligible"} - {returns.instructions}</div>
        )}
        {refund && (
          <div><b>Refund:</b> {refund.refundStatus} - Amount: ${refund.amount}</div>
        )}
        {faq.length > 0 && (
          <div><b>FAQ:</b><ul>{faq.map((f, i) => <li key={i}>{f.q} <br/><i>{f.a}</i></li>)}</ul></div>
        )}
        {kb.length > 0 && (
          <div><b>Knowledge Base:</b><ul>{kb.map((k, i) => <li key={i}><b>{k.title}:</b> {k.content}</li>)}</ul></div>
        )}
      </div>
      <div style={{ marginTop: 32, fontSize: 14, color: '#888' }}>
        <b>Note:</b> All automations (auto-assign, tagging, escalation, etc.) are managed in BoldDesk dashboard.
      </div>
    </div>
  );
};

export default HomePage;
