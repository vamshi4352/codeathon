# API Configuration - Request and Response Payloads

## Endpoint Details

### 1. Enhancement Endpoint: `/api/products`

**Purpose**: Retrieve product performance metrics for inventory management.

#### BEFORE Enhancement (Current Working State)
**Request**: `GET /api/products`

**Response Payload**:
```json
{
  "products": [
    {
      "product_name": "Gaming Laptop",
      "price": 1299.99,
      "total_count": 2
    },
    {
      "product_name": "Test Widget",
      "price": 99.99,
      "total_count": 8
    }
  ],
  "total_products": 20
}
```

#### AFTER Enhancement (Required Implementation)
**Request**: `GET /api/products`

**Enhanced Response Payload**:
```json
{
  "products": [
    {
      "product_name": "Gaming Laptop",
      "price": 1299.99,
      "total_count": 2,
      "average_rating": 4.5,
      "total_revenue": 2599.98,
      "category": "Electronics"
    },
    {
      "product_name": "Test Widget",
      "price": 99.99,
      "total_count": 8,
      "average_rating": 4.5,
      "total_revenue": 799.92,
      "category": "Electronics"
    }
  ],
  "total_products": 20,
  "summary": {
    "total_revenue": 45678.90,
    "average_product_rating": 4.3,
    "top_performer": "Gaming Laptop",
    "lowest_performer": "Basic Pen"
  }
}
```

---

### 2. Easy Debug Endpoint: `/api/dashboard`

**Purpose**: Generate executive dashboard summary with key business metrics.

#### Current Implementation (Broken)
**Request**: `GET /api/dashboard?days=30`

**Buggy Response Payload**:
```json
{
  "period_days": 30,
  "total_revenue": 150.00,
  "total_transactions": 5,
  "average_order_value": 2.1,
  "average_rating": 4.9,
  "data_points": 2
}
```

#### Fixed Implementation (Expected)
**Request**: `GET /api/dashboard?days=30`

**Correct Response Payload**:
```json
{
  "period_days": 30,
  "total_revenue": 15420.75,
  "total_transactions": 85,
  "average_order_value": 181.42,
  "average_rating": 4.3,
  "data_points": 85
}
```

---

### 3. Intermediate Debug Endpoint: `/api/categories`

**Purpose**: Analyze category performance metrics for merchandising decisions.

#### Current Implementation (Broken)
**Request**: `GET /api/categories`

**Buggy Response Payload**:
```json
{
  "categories": [
    {
      "total_revenue": 1299.99,
      "avg_revenue_per_transaction": 150.50,
      "transaction_count": 15,
      "avg_rating": 4.2,
      "total_units_sold": 25,
      "revenue_percentage": 2.5
    }
  ],
  "total_categories": 1
}
```

#### Fixed Implementation (Expected)
**Request**: `GET /api/categories`

**Correct Response Payload**:
```json
{
  "categories": [
    {
      "category": "Electronics",
      "total_revenue": 12456.78,
      "avg_revenue_per_transaction": 185.42,
      "transaction_count": 67,
      "avg_rating": 4.4,
      "total_units_sold": 89,
      "revenue_percentage": 35.2
    },
    {
      "category": "Clothing",
      "total_revenue": 8234.56,
      "avg_revenue_per_transaction": 98.23,
      "transaction_count": 84,
      "avg_rating": 4.1,
      "total_units_sold": 112,
      "revenue_percentage": 23.3
    }
  ],
  "total_categories": 6
}
```

---

### 4. Build-from-Scratch Endpoint: `/api/demographics`

**Purpose**: Analyze customer demographics for targeted marketing campaigns.

#### Required Implementation
**Request**: `GET /api/demographics`

**Expected Response Payload**:
```json
{
  "age_groups": [
    {
      "age_range": "18-25",
      "customer_count": 45,
      "avg_spending": 87.50,
      "total_revenue": 3937.50,
      "avg_rating": 4.2,
      "transaction_count": 58,
      "revenue_percentage": 11.2
    },
    {
      "age_range": "26-35",
      "customer_count": 78,
      "avg_spending": 142.30,
      "total_revenue": 11099.40,
      "avg_rating": 4.4,
      "transaction_count": 89,
      "revenue_percentage": 31.5
    },
    {
      "age_range": "36-45",
      "customer_count": 65,
      "avg_spending": 165.80,
      "total_revenue": 10777.00,
      "avg_rating": 4.3,
      "transaction_count": 72,
      "revenue_percentage": 30.6
    },
    {
      "age_range": "46-55",
      "customer_count": 38,
      "avg_spending": 198.20,
      "total_revenue": 7531.60,
      "avg_rating": 4.5,
      "transaction_count": 45,
      "revenue_percentage": 21.4
    },
    {
      "age_range": "56+",
      "customer_count": 24,
      "avg_spending": 215.40,
      "total_revenue": 5169.60,
      "avg_rating": 4.6,
      "transaction_count": 28,
      "revenue_percentage": 14.7
    }
  ],
  "summary": {
    "total_customers": 250,
    "highest_spending_group": "56+",
    "largest_group": "26-35",
    "highest_rated_group": "56+"
  }
}
```

---

### 5. Complex Build-from-Scratch Endpoint: `/api/revenue-insights`

**Purpose**: Generate comprehensive revenue insights for strategic planning.

#### Required Implementation
**Request**: `GET /api/revenue-insights`

**Expected Response Payload**:
```json
{
  "monthly_trends": [
    {
      "month": "2024-01",
      "revenue": 5240.75,
      "transaction_count": 45,
      "growth_rate": null
    },
    {
      "month": "2024-02",
      "revenue": 6150.30,
      "transaction_count": 52,
      "growth_rate": 17.4
    },
    {
      "month": "2024-03",
      "revenue": 5890.45,
      "transaction_count": 48,
      "growth_rate": -4.2
    }
  ],
  "top_products": [
    {
      "product_name": "Premium Laptop",
      "total_revenue": 1999.99,
      "revenue_contribution": 5.7,
      "rank": 1
    },
    {
      "product_name": "Luxury Watch",
      "total_revenue": 1299.99,
      "revenue_contribution": 3.7,
      "rank": 2
    }
  ],
  "category_distribution": [
    {
      "category": "Electronics",
      "revenue": 12456.78,
      "percentage": 35.4
    },
    {
      "category": "Clothing",
      "revenue": 8234.56,
      "percentage": 23.4
    }
  ],
  "customer_segments": [
    {
      "segment": "High Value",
      "customer_count": 25,
      "avg_order_value": 285.60,
      "total_revenue": 7140.00,
      "criteria": "Orders > $200"
    },
    {
      "segment": "Medium Value",
      "customer_count": 120,
      "avg_order_value": 125.80,
      "total_revenue": 15096.00,
      "criteria": "Orders $50-$200"
    },
    {
      "segment": "Low Value",
      "customer_count": 105,
      "avg_order_value": 32.40,
      "total_revenue": 3402.00,
      "criteria": "Orders < $50"
    }
  ],
  "growth_metrics": {
    "overall_growth_rate": 8.7,
    "revenue_trend": "increasing",
    "best_performing_month": "2024-02",
    "seasonal_pattern": "slight_decline_in_march"
  },
  "forecasting": {
    "predicted_next_month_revenue": 6250.00,
    "confidence_level": "medium",
    "key_drivers": ["electronics_sales", "customer_retention"]
  }
}
```

## Error Response Format

All endpoints should return consistent error responses:

```json
{
  "detail": "Error description",
  "status_code": 500,
  "timestamp": "2024-07-18T10:30:00Z"
}
```

## Query Parameters

### Dashboard Endpoint
- `days` (optional): Number of days to look back (1-180, default: 30)

Example: `GET /api/dashboard?days=60`

## Notes

- All monetary values should be rounded to 2 decimal places
- Percentages should be rounded to 1 decimal place
- Dates should be in ISO format (YYYY-MM-DD)
- Missing ratings should be excluded from average calculations
- Growth rates are calculated as: ((current - previous) / previous) * 100