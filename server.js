const express = require('express');
const path = require('path');
const app = express();
const PORT = 5000;

// Demo: Order Status (with orderId)
app.get('/api/order-status', (req, res) => {
  const { orderId } = req.query;
  if (!orderId) {
    return res.status(400).json({ error: 'Missing orderId' });
  }
  // Demo: Only ORD12345 is valid for mock
  if (orderId === 'ORD12345') {
    return res.json({
      orderId,
      status: 'Shipped',
      estimatedDelivery: '2025-09-20',
      customer: 'Jane Doe'
    });
  }
  return res.status(404).json({ error: 'Order not found' });
});

// Demo: Returns (with orderId)
app.get('/api/returns', (req, res) => {
  const { orderId } = req.query;
  if (!orderId) {
    return res.status(400).json({ error: 'Missing orderId' });
  }
  if (orderId === 'ORD12346') {
    return res.json({
      orderId,
      returnEligible: true,
      reason: 'Within 30 days',
      instructions: 'Use the prepaid label to return your item.'
    });
  }
  return res.status(404).json({ error: 'Order not found or not eligible for return' });
});

// Demo: Refunds (with orderId)
app.get('/api/refunds', (req, res) => {
  const { orderId } = req.query;
  if (!orderId) {
    return res.status(400).json({ error: 'Missing orderId' });
  }
  if (orderId === 'ORD12347') {
    return res.json({
      orderId,
      refundStatus: 'Pending',
      amount: 49.99,
      method: 'Original payment method'
    });
  }
  return res.status(404).json({ error: 'Order not found or not eligible for refund' });
});

// Demo: FAQ
app.get('/api/faq', (req, res) => {
  res.json([
    { q: 'How do I track my order?', a: 'Use the order status page.' },
    { q: 'How do I request a return?', a: 'Go to your orders and select return.' }
  ]);
});

// Demo: Knowledge Base
app.get('/api/kb', (req, res) => {
  res.json([
    { id: 1, title: 'Return Policy', content: 'Returns accepted within 30 days.' },
    { id: 2, title: 'Refund Process', content: 'Refunds processed within 5 business days.' }
  ]);
});

app.use(express.static(path.join(__dirname, 'build')));
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});