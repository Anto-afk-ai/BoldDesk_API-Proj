# Mock product/item list for API usage
ITEMS = [
	{
		"id": 'ELC12',
		"name": "Wireless Mouse",
		"category": "Electronics",
		"price": 19.99,
		"stock": 120,
		"description": "Ergonomic wireless mouse with USB receiver.",
		"sku": "WM-1001"
	},
	{
		"id": 'ELC22',
		"name": "Bluetooth Headphones",
		"category": "Electronics",
		"price": 49.99,
		"stock": 80,
		"description": "Over-ear headphones with noise cancellation.",
		"sku": "BH-2002"
	},
	{
		"id": 'YMC30',
		"name": "Yoga Mat",
		"category": "Fitness",
		"price": 25.00,
		"stock": 200,
		"description": "Non-slip yoga mat for all exercises.",
		"sku": "YM-3003"
	},
	{
		"id": 'SWB40',
		"name": "Stainless Steel Water Bottle",
		"category": "Outdoors",
		"price": 15.50,
		"stock": 150,
		"description": "Insulated bottle keeps drinks cold for 24h.",
		"sku": "WB-4004"
	},
	{
		"id": 'DL551',
		"name": "Desk Lamp",
		"category": "Home",
		"price": 29.99,
		"stock": 60,
		"description": "LED desk lamp with adjustable brightness.",
		"sku": "DL-5005"
	},
	{
		"id": 'SH0011',
		"name": "Running Shoes",
		"category": "Footwear",
		"price": 75.00,
		"stock": 45,
		"description": "Lightweight running shoes for men and women.",
		"sku": "RS-6006"
	},
	{
		"id": 'WW1120',
		"name": "Smart Watch",
		"category": "Electronics",
		"price": 120.00,
		"stock": 30,
		"description": "Fitness tracking smart watch with heart rate monitor.",
		"sku": "SW-7007"
	},
	{
		"id": 'EEC010',
		"name": "Coffee Maker",
		"category": "Kitchen",
		"price": 59.99,
		"stock": 25,
		"description": "Automatic drip coffee maker with timer.",
		"sku": "CM-8008"
	},
	{
		"id": 'ASC01',
		"name": "Backpack",
		"category": "Accessories",
		"price": 39.99,
		"stock": 90,
		"description": "Water-resistant backpack for travel and school.",
		"sku": "BP-9009"
	},
	{
		"id": 'EEC2201',
		"name": "Electric Toothbrush",
		"category": "Personal Care",
		"price": 34.99,
		"stock": 70,
		"description": "Rechargeable electric toothbrush with 3 modes.",
		"sku": "ET-1010"
	}
]

ORDER_STATUS = [
	{ 
        "id" : "ORD12345",
		"status": "Shipped",
		"estimated_delivery": "2024-10-05",
		"tracking_number": "TRACK123456",
		"carrier": "FastShip",
		"items": [
			{"id": 'ELC12', "name": "Wireless Mouse", "quantity": 1},
			{"id": 'SWB40', "name": "Stainless Steel Water Bottle", "quantity": 2}
		],
		"total_amount": 50.99,
		"shipping_address": "123 Main St, Anytown, USA",
		"sku": "WM-1001"
	},
	{
        "id" : "ORD12346", 
		"status": "Processing",
		"estimated_delivery": "2024-10-10",
		"tracking_number": None,
		"carrier": None,
		"items": [
			{"id": 'YMC30', "name": "Yoga Mat", "quantity": 1}
		],
		"total_amount": 25.00,
		"shipping_address": "456 Oak Ave, Sometown, USA",
		"sku": "YM-3003"
	},
	{
        "id" : "ORD12347",
		"status": "Delivered",
		"estimated_delivery": "2024-09-20",
		"tracking_number": "TRACK654321",
		"carrier": "QuickDelivery",
		"items": [
			{"id": 'DL551', "name": "Desk Lamp", "quantity": 1},
			{"id": 'EEC010', "name": "Coffee Maker", "quantity": 1}
		],
		"total_amount": 89.98,
		"shipping_address": "789 Pine Rd, Yourtown, USA",
		"sku": "DL-5005"
	}
]
