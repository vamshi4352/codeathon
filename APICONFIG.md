# API Configuration - Request and Response Payloads

## Endpoint Details

### 1. Enhancement Endpoint: `/api/products`

**Purpose**: Retrieve product performance metrics for inventory management.

#### BEFORE Enhancement (Current Working State)
**Request**: `GET /api/products`

**Current Response Payload**:
```json
{
  "products": [
    {
      "product_name": "Gaming Laptop"
    },
    {
      "product_name": "Test Widget"
    }
  ],
  "total_products": 20,
  "summary": {
    "total_revenue": 45678.90
  }
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

**Enhancement Requirements**:
- Add `price` field for each product (current product price)
- Add `total_count` field for each product (total units sold)
- Add `average_rating` field for each product (average customer rating, null if no ratings)
- Add `total_revenue` field for each product (total revenue generated)
- Add `category` field for each product (product category)
- Enhance summary section with `average_product_rating`, `top_performer`, and `lowest_performer`

---

### 2. Debug Endpoint: `/api/categories`

**Purpose**: Analyze category performance metrics for merchandising decisions.

#### Current Implementation (Broken - 5 Bugs Present)
**Request**: `GET /api/categories`

**Buggy Response Payload** (Contains Data Science Errors):
```json
{
  "categories": [
    {
      "category": "Electronics",
      "total_revenue": 1299.99,
      "avg_revenue_per_transaction": 150.50,
      "transaction_count": 15,
      "avg_rating": 4.2,
      "total_units_sold": 25,
      "revenue_percentage": 2.5
    }
  ],
  "total_categories": 25
}
```

#### Fixed Implementation (Expected After Debug)
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
    },
    {
      "category": "Books",
      "total_revenue": 3456.78,
      "avg_revenue_per_transaction": 45.67,
      "transaction_count": 76,
      "avg_rating": 4.6,
      "total_units_sold": 98,
      "revenue_percentage": 9.8
    },
    {
      "category": "Home",
      "total_revenue": 5678.90,
      "avg_revenue_per_transaction": 67.89,
      "transaction_count": 84,
      "avg_rating": 4.2,
      "total_units_sold": 123,
      "revenue_percentage": 16.1
    },
    {
      "category": "Sports",
      "total_revenue": 2345.67,
      "avg_revenue_per_transaction": 34.56,
      "transaction_count": 68,
      "avg_rating": 4.3,
      "total_units_sold": 89,
      "revenue_percentage": 6.6
    },
    {
      "category": "Beauty",
      "total_revenue": 2987.65,
      "avg_revenue_per_transaction": 43.21,
      "transaction_count": 69,
      "avg_rating": 4.5,
      "total_units_sold": 87,
      "revenue_percentage": 8.5
    }
  ],
  "total_categories": 6
}
```

**Debug Requirements**:
- Fix aggregation method errors (using wrong aggregation functions)
- Correct column reference mistakes (using wrong columns for calculations)
- Add proper error handling for division by zero scenarios
- Fix data type and NaN value handling issues
- Correct count calculations using appropriate data columns

---

### 3. Build-from-Scratch Endpoint: `/api/revenue-insights`

**Purpose**: Generate comprehensive revenue insights for strategic planning.

#### Current Implementation (Empty - Placeholder Data Only)
**Request**: `GET /api/revenue-insights`

**Current Placeholder Response**:
```json
{
  "monthly_trends": [
    {"month": "2024-01", "revenue": 0.0, "transaction_count": 0, "growth_rate": null},
    {"month": "2024-02", "revenue": 0.0, "transaction_count": 0, "growth_rate": 0.0}
  ],
  "top_products": [
    {"product_name": "placeholder", "total_revenue": 0.0, "revenue_contribution": 0.0, "rank": 1},
    {"product_name": "placeholder", "total_revenue": 0.0, "revenue_contribution": 0.0, "rank": 2}
  ],
  "category_distribution": [
    {"category": "placeholder", "revenue": 0.0, "percentage": 0.0}
  ],
  "customer_segments": [
    {"segment": "High Value", "customer_count": 0, "avg_order_value": 0.0, "total_revenue": 0.0, "criteria": "Orders > $200"},
    {"segment": "Medium Value", "customer_count": 0, "avg_order_value": 0.0, "total_revenue": 0.0, "criteria": "Orders $50-$200"},
    {"segment": "Low Value", "customer_count": 0, "avg_order_value": 0.0, "total_revenue": 0.0, "criteria": "Orders < $50"}
  ],
  "growth_metrics": {
    "overall_growth_rate": 0.0,
    "revenue_trend": "insufficient_data",
    "best_performing_month": null,
    "seasonal_pattern": "slight_decline_in_march"
  },
  "forecasting": {
    "predicted_next_month_revenue": 0.0,
    "confidence_level": "medium",
    "key_drivers": ["electronics_sales", "customer_retention"]
  }
}
```

#### Required Implementation (Complete Functionality Needed)
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
    },
    {
      "month": "2024-04",
      "revenue": 6420.85,
      "transaction_count": 55,
      "growth_rate": 9.0
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
    },
    {
      "category": "Books",
      "revenue": 3456.78,
      "percentage": 9.8
    },
    {
      "category": "Home",
      "revenue": 5678.90,
      "percentage": 16.1
    },
    {
      "category": "Sports",
      "revenue": 2345.67,
      "percentage": 6.7
    },
    {
      "category": "Beauty",
      "revenue": 2987.65,
      "percentage": 8.5
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

**Implementation Requirements**:

1. **Monthly Trends Analysis**:
   - Group transactions by month (YYYY-MM format)
   - Calculate total revenue and transaction count per month
   - Calculate month-over-month growth rates: `((current - previous) / previous) * 100`
   - First month should have `null` growth rate

2. **Top Products Analysis** (Limit to Top 2):
   - Rank products by total revenue
   - Calculate revenue contribution percentage
   - Include rank field (1, 2)

3. **Category Distribution**:
   - Calculate total revenue per category
   - Calculate percentage of total revenue for each category
   - Include all categories present in data

4. **Customer Segmentation**:
   - Segment customers based on individual transaction revenue:
     - High Value: revenue > $200
     - Medium Value: revenue $50-$200  
     - Low Value: revenue < $50
   - Calculate customer count, average order value, and total revenue per segment

5. **Growth Metrics**:
   - Calculate overall growth rate (recent month vs previous)
   - Determine revenue trend (increasing/decreasing/stable)
   - Identify best performing month by revenue
   - Include seasonal pattern analysis

6. **Forecasting**:
   - Predict next month revenue (simple average of last 3 months + 5% growth)
   - Include confidence level and key business drivers

## Error Response Format

All endpoints should return consistent error responses:

```json
{
  "detail": "Error description",
  "status_code": 500,
  "timestamp": "2024-07-18T10:30:00Z"
}
```

## Data Formatting Requirements

- **Monetary values**: Round to 2 decimal places
- **Percentages**: Round to 1 decimal place  
- **Dates**: Use ISO format (YYYY-MM) for months
- **Missing ratings**: Exclude from average calculations, return `null` if no ratings available
- **Growth rates**: Calculate as `((current - previous) / previous) * 100`
- **Customer segments**: Based on individual transaction revenue, not customer lifetime value

## Testing Data Notes

- Dataset contains "Test Widget" products for automated evaluation
- Date range spans approximately 6 months (Jan-Aug 2024)
- Customer ratings may have missing values (handle appropriately)
- Categories include: Electronics, Clothing, Books, Home, Sports, Beauty