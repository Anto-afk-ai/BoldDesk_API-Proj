# Mock product/item list for API usage
ITEMS = [
    {
        "id": 'COF001',
        "name": "Premium Arabica Coffee Beans",
        "category": "Coffee Beans",
        "price": 24.99,
        "stock": 500,
        "description": "Premium whole bean Arabica coffee, perfect for offices and cafes. (1kg bag)",
        "sku": "ARB-1001",
        "bulk_options": [
            {"quantity": 5, "discount": 10},
            {"quantity": 10, "discount": 15},
            {"quantity": 20, "discount": 20}
        ],
		"imageUrl": "Coffee-beans.png"
    },
    {
        "id": 'COF002',
        "name": "Colombian Dark Roast",
        "category": "Coffee Beans",
        "price": 22.99,
        "stock": 500,
        "description": "Rich, dark roasted Colombian coffee beans. Perfect for espresso. (1kg bag)",
        "sku": "CDR-1002",
        "bulk_options": [
            {"quantity": 5, "discount": 10},
            {"quantity": 10, "discount": 15},
            {"quantity": 20, "discount": 20}
        ],
        "imageUrl": "Colombian-dark-roast.png"
    },
    {
        "id": 'COF003',
        "name": "House Blend Ground Coffee",
        "category": "Ground Coffee",
        "price": 19.99,
        "stock": 400,
        "description": "Pre-ground medium roast blend, perfect for drip coffee makers. (1kg bag)",
        "sku": "HBG-1003",
        "bulk_options": [
            {"quantity": 5, "discount": 10},
            {"quantity": 10, "discount": 15},
            {"quantity": 20, "discount": 20}
        ],
        "imageUrl": "House-blendg-ground-coffee.png"
    },
    {
        "id": 'SNK001',
        "name": "Gourmet Coffee Cookies",
        "category": "Snacks",
        "price": 15.99,
        "stock": 200,
        "description": "Coffee-flavored butter cookies, perfect complement to coffee. (Box of 24)",
        "sku": "GCC-2001",
        "bulk_options": [
            {"quantity": 5, "discount": 8},
            {"quantity": 10, "discount": 12},
            {"quantity": 20, "discount": 15}
        ],
        "imageUrl": "Gourmet-coffee-cokies.png"
    },
    {
        "id": 'SNK002',
        "name": "Chocolate Covered Coffee Beans",
        "category": "Snacks",
        "price": 18.99,
        "stock": 150,
        "description": "Premium coffee beans covered in dark chocolate. (500g bag)",
        "sku": "CCB-2002",
        "bulk_options": [
            {"quantity": 5, "discount": 8},
            {"quantity": 10, "discount": 12},
            {"quantity": 20, "discount": 15}
        ],
        "imageUrl": "Covered-coffee-beans.png"
    },
    {
        "id": 'EQP001',
        "name": "Commercial Coffee Filter Papers",
        "category": "Equipment",
        "price": 29.99,
        "stock": 300,
        "description": "Professional-grade coffee filter papers. (Box of 200)",
        "sku": "CFP-3001",
        "bulk_options": [
            {"quantity": 5, "discount": 10},
            {"quantity": 10, "discount": 15},
            {"quantity": 20, "discount": 20}
        ],
        "imageUrl": "Filter-papers.png"
    },
    {
        "id": 'EQP002',
        "name": "Coffee Machine Cleaning Kit",
        "category": "Equipment",
        "price": 34.99,
        "stock": 100,
        "description": "Professional cleaning supplies for coffee machines and grinders.",
        "sku": "CCK-3002",
        "bulk_options": [
            {"quantity": 3, "discount": 5},
            {"quantity": 5, "discount": 10},
            {"quantity": 10, "discount": 15}
        ],
		"imageUrl": "Cleaning-kit.png"
    }
]

ORDERS = [
    {"anto.sf3688@gmail.com":[
        {
        "id": "ORD20001",
        "status": "Out for Delivery",
        "estimated_delivery": "2025-10-12",
        "tracking_number": "TRACK200001",
        "carrier": "FastShip",
        "items": [
            {"id": "COF001", "name": "Premium Arabica Coffee Beans", "quantity": 2, "price": 24.99, "sku": "ARB-1001", "subtotal": 49.98},
            {"id": "SNK001", "name": "Gourmet Coffee Cookies", "quantity": 1, "price": 15.99, "sku": "GCC-2001", "subtotal": 15.99}
        ],
        "order_total": 65.97,
        "shipping_address": "12 Brew Lane, Roastville, USA"
		},
		{
			"id": "ORD20002",
			"status": "Processing",
			"estimated_delivery": "2025-10-18",
			"tracking_number": None,
			"carrier": None,
			"items": [
				{"id": "COF002", "name": "Colombian Dark Roast", "quantity": 3, "price": 22.99, "sku": "CDR-1002", "subtotal": 68.97},
				{"id": "EQP002", "name": "Coffee Machine Cleaning Kit", "quantity": 1, "price": 34.99, "sku": "CCK-3002", "subtotal": 34.99}
			],
			"order_total": 103.96,
			"shipping_address": "34 Espresso Ave, Bean City, USA"
		},
		{
			"id": "ORD20003",
			"status": "Delivered",
			"estimated_delivery": "2025-09-30",
			"tracking_number": "TRACK200003",
			"carrier": "QuickDelivery",
			"items": [
				{"id": "COF003", "name": "House Blend Ground Coffee", "quantity": 1, "price": 19.99, "sku": "HBG-1003", "subtotal": 19.99},
				{"id": "SNK002", "name": "Chocolate Covered Coffee Beans", "quantity": 2, "price": 18.99, "sku": "CCB-2002", "subtotal": 37.98},
				{"id": "EQP001", "name": "Commercial Coffee Filter Papers", "quantity": 1, "price": 29.99, "sku": "CFP-3001", "subtotal": 29.99}
			],
			"order_total": 87.96,
			"shipping_address": "12 Brew Lane, Roastville, USA"
		}
	]}
];
