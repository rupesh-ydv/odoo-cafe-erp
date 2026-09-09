# Product Accessories Module
## Cafe ERP eCommerce System

---

# 1. Introduction

The **Product Accessories** module is a custom Odoo 19 eCommerce module developed for a Cafe ERP system.

The purpose of the module is to allow cafe administrators to configure complementary or additional products that can be recommended to customers when they are viewing a main product on the eCommerce website.

For example, when a customer views a **Chicken Burger**, the system can recommend products such as:

- French Fries
- Coca-Cola
- Extra Cheese
- Sauce

This functionality improves the customer's online ordering experience and provides the cafe with a structured way to manage related products.

The module extends Odoo's existing eCommerce functionality rather than replacing the standard product, sales, cart, or inventory systems.

---

# 2. Problem Statement

## 2.1 Existing Problem

In a cafe eCommerce system, customers often purchase products together with complementary items.

For example:

- Burger with French Fries
- Burger with a soft drink
- Pizza with a beverage
- Coffee with extra syrup
- Sandwich with chips

Without a dedicated product accessory feature, customers may need to search for these additional products separately.

This can result in:

- Difficulty discovering complementary products.
- A less convenient ordering experience.
- Missed opportunities to offer relevant add-on products.
- Difficulty managing product-to-product accessory relationships.
- The possibility of displaying products that are inactive, unpublished, or not available for sale.
- Additional manual configuration or handling by cafe staff.

Therefore, a custom Product Accessories module is required to provide controlled management and display of related products.

---

# 3. Proposed Solution

The proposed solution is a custom Odoo 19 module named:

**Product Accessories**

Technical module name:

```text
product_accessories
```

The module allows administrators to associate one or more accessory products with a main product.

The configured accessories can then be displayed on the corresponding eCommerce product page.

The system validates the accessory products before displaying them to customers.

This ensures that only appropriate products are presented as accessories.

---

# 4. Objectives

The main objectives of the Product Accessories module are:

1. Allow administrators to configure accessories for products.
2. Display relevant accessories on the eCommerce product page.
3. Allow optional accessories to be selected by customers.
4. Support required accessories where applicable.
5. Validate accessory products before displaying them.
6. Prevent inactive products from being displayed as accessories.
7. Prevent non-saleable products from being displayed as accessories.
8. Prevent unpublished products from being displayed as website accessories.
9. Display accessory product names, prices, and images.
10. Integrate selected accessories with the normal Odoo eCommerce ordering process.

---

# 5. Scope of the Module

The Product Accessories module focuses specifically on the relationship between a main product and its accessory products.

### Included in the module

- Accessory configuration.
- Accessory activation and deactivation.
- Accessory website publication control.
- Accessory validation.
- Optional accessory configuration.
- Required accessory configuration.
- Accessory product name display.
- Accessory price display.
- Accessory image display.
- eCommerce product-page integration.
- Integration with the Odoo sales order process.

### Outside the primary scope

The module does not replace Odoo's:

- Standard product management.
- Standard shopping cart.
- Standard sales order management.
- Standard inventory management.
- Standard delivery management.
- Standard payment provider system.

These existing Odoo features continue to manage their respective processes.

---

# 6. Module Functionality

## 6.1 Accessory Configuration

The administrator can configure accessories for a main product.

For example:

| Main Product | Accessory |
|---|---|
| Chicken Burger | French Fries |
| Chicken Burger | Coca-Cola |
| Chicken Burger | Extra Cheese |
| Pizza | Soft Drink |
| Coffee | Extra Syrup |

This creates a structured relationship between the main product and its related accessories.

---

## 6.2 Optional Accessories

An accessory can be configured as optional.

For example:

**Chicken Burger**

Optional accessories:

- French Fries
- Coca-Cola
- Extra Cheese

The customer can select the accessories they want.

This allows customers to customize their order according to their preferences.

---

## 6.3 Required Accessories

The module can also support required accessories.

For example, a cafe may define a particular add-on as required for a specific product configuration.

A required accessory can be automatically selected on the website and should be handled appropriately during the ordering process.

Server-side validation should be used if the business rule requires the accessory to be mandatory.

---

## 6.4 Accessory Activation

Each accessory relationship can be activated or deactivated.

For example:

```text
French Fries
Active: Yes
```

means the accessory relationship can be used.

If:

```text
French Fries
Active: No
```

the accessory should not be displayed.

This allows cafe administrators to temporarily disable an accessory without removing its configuration.

---

# 7. Accessory Validation

Validation is an important part of the Product Accessories module.

The module should display an accessory only when the required conditions are satisfied.

| Condition | Required |
|---|---|
| Accessory relationship is active | Yes |
| Accessory is website published | Yes |
| Accessory product is active | Yes |
| Accessory product can be sold | Yes |

For example, if a product is configured as an accessory but **Can be Sold** is disabled, it should not be displayed as a valid eCommerce accessory.

Similarly, an unpublished product should not be displayed to website customers.

---

# 8. Website Integration

The Product Accessories module integrates with the Odoo eCommerce product page.

When a customer opens a product that has valid accessories, the website displays an accessory section.

For example:

### Chicken Burger

**Price:** Rs. 450

### Add Accessories

| Select | Accessory | Price |
|---|---|---:|
| ☑ | French Fries | Rs. 150 |
| ☐ | Coca-Cola | Rs. 100 |
| ☐ | Extra Cheese | Rs. 80 |

The customer can select the desired accessories before adding the products to the cart.

If the main product has no valid accessories, the accessory section should not be displayed.

---

# 9. Accessory Information Displayed

The website accessory section can display:

- Accessory product name.
- Accessory product image.
- Accessory price.
- Required/optional status.
- Accessory selection checkbox.

This provides customers with useful information before they add accessories to their order.

---

# 10. Cafe ERP Use Case

The Product Accessories module is particularly useful for a cafe ERP system because cafe products commonly have complementary items.

### Example 1: Burger

**Main Product:**

Chicken Burger — Rs. 450

**Accessories:**

- French Fries — Rs. 150
- Coca-Cola — Rs. 100
- Extra Cheese — Rs. 80

### Example 2: Pizza

**Main Product:**

Chicken Pizza — Rs. 700

**Accessories:**

- Soft Drink — Rs. 100
- Garlic Bread — Rs. 180
- Extra Cheese — Rs. 100

### Example 3: Coffee

**Main Product:**

Cappuccino — Rs. 250

**Accessories:**

- Extra Syrup — Rs. 50
- Chocolate — Rs. 70
- Cookie — Rs. 80

This allows the cafe to provide relevant recommendations for different products.

---

# 11. Cart and Sales Order Integration

When a customer selects accessories, the selected products should be included in the eCommerce order.

For example:

| Product | Quantity |
|---|---:|
| Chicken Burger | 1 |
| French Fries | 1 |
| Coca-Cola | 1 |

The accessories should be represented as separate sale order lines where the module is designed to add them as independent products.

This allows Odoo's standard Sales functionality to process the products normally.

---

# 12. Inventory Consideration

The Product Accessories module should not directly modify inventory simply because an accessory is selected or added to the cart.

For example:

```text
French Fries
On Hand = 10
```

A customer selecting French Fries as an accessory does not by itself mean that the physical inventory should immediately become:

```text
On Hand = 9
```

Inventory remains managed by Odoo's standard inventory and sales processes.

This separation is important because:

- Cart selection is not the same as product delivery.
- Sales orders and stock operations are separate processes.
- Inventory should be updated through Odoo's standard stock operations.

The Product Accessories module therefore focuses on product relationships and eCommerce ordering rather than directly manipulating inventory quantities.

---

# 13. Functional Validation

The module should be tested using different product and accessory conditions.

## 13.1 Valid Accessory Test

**Condition:**

- Accessory active.
- Product active.
- Product can be sold.
- Product published on website.

**Expected result:**

The accessory appears on the product page.

---

## 13.2 Inactive Accessory Test

**Condition:**

Accessory relationship is inactive.

**Expected result:**

The accessory is not displayed.

---

## 13.3 Unpublished Accessory Test

**Condition:**

Accessory product is not published on the website.

**Expected result:**

The accessory is not displayed to website customers.

---

## 13.4 Non-Saleable Accessory Test

**Condition:**

The accessory product has **Can be Sold** disabled.

**Expected result:**

The accessory is not displayed as an available eCommerce accessory.

---

## 13.5 No Accessory Test

**Condition:**

The main product has no valid accessories.

**Expected result:**

The Product Accessories section is hidden from the product page.

---

## 13.6 Multiple Accessories Test

**Condition:**

A product has multiple valid accessories.

**Expected result:**

All valid accessories are displayed.

For example:

| Accessory | Status |
|---|---|
| French Fries | Displayed |
| Coca-Cola | Displayed |
| Extra Cheese | Displayed |

---

# 14. User Acceptance Testing

The following tests can be used to validate the module from the user's perspective.

| Test Case | Expected Result | Status |
|---|---|---|
| Create main product | Product created successfully | Pass/Fail |
| Create accessory product | Product created successfully | Pass/Fail |
| Configure accessory | Accessory saved successfully | Pass/Fail |
| Publish accessory | Accessory available on website | Pass/Fail |
| Disable accessory | Accessory hidden | Pass/Fail |
| Disable Can Be Sold | Accessory hidden | Pass/Fail |
| Open product page | Accessories displayed | Pass/Fail |
| Select optional accessory | Accessory selected | Pass/Fail |
| Add product to cart | Product added successfully | Pass/Fail |
| Add accessory to order | Accessory included in order | Pass/Fail |
| Checkout | Order processed normally | Pass/Fail |

---

# 15. Benefits of the Product Accessories Module

## 15.1 Customer Benefits

- Makes complementary products easier to discover.
- Provides a more convenient ordering experience.
- Allows customers to customize their orders.
- Displays accessory information directly on the product page.
- Reduces the need to search for related products separately.

## 15.2 Cafe Benefits

- Makes accessory management easier.
- Provides opportunities for cross-selling.
- Allows administrators to control which accessories are displayed.
- Prevents invalid products from being presented as accessories.
- Supports a more organized eCommerce product catalog.

## 15.3 System Benefits

- Extends Odoo 19 eCommerce functionality.
- Uses existing Odoo product and sales information.
- Maintains compatibility with the standard sales process.
- Provides a reusable accessory-management structure.
- Can be further extended for future cafe-specific requirements.

---

# 16. Limitations and Considerations

The Product Accessories module is intended to extend Odoo's standard eCommerce functionality.

The following considerations should be taken into account:

- Accessory validation should be performed on the server as well as the website where necessary.
- Required accessory rules should not rely only on a website checkbox.
- Inventory should be managed through Odoo's standard stock workflow.
- The module should respect Odoo's product and website publication settings.
- Selected accessories should be validated before being added to a sales order.

These considerations help maintain data consistency and prevent customers from ordering invalid products.

---

# 17. Findings

The development and validation of the Product Accessories module demonstrate that:

1. Product accessories are useful for a cafe-based eCommerce system.
2. Cafe products commonly have related complementary products.
3. A dedicated accessory configuration improves product relationship management.
4. Accessory validation prevents invalid products from being displayed.
5. Website integration makes accessories easier for customers to discover.
6. Optional accessories provide customers with greater flexibility.
7. Required accessories can be used when specific business rules require them.
8. Selected accessories can be integrated with the normal Odoo sales order process.
9. The module does not need to directly modify inventory quantities.
10. The Product Accessories module can extend Odoo 19 eCommerce without replacing its standard functionality.

---

# 18. Conclusion

The **Product Accessories** module provides a focused customization for the Odoo 19 eCommerce system used in the Cafe ERP environment.

The module addresses the problem of managing and presenting complementary products by allowing cafe administrators to configure accessories for individual products and control their availability for website display.

Through accessory validation, the system ensures that inactive, unpublished, or non-saleable products are not unnecessarily presented to customers.

The module also improves the customer experience by displaying relevant accessory products, prices, images, and selection options directly on the main product page.

The functionality is designed to integrate with Odoo's existing eCommerce and Sales processes while leaving inventory management to the standard Odoo stock workflow.

Overall, the **Product Accessories** module provides a practical and reusable enhancement for cafe eCommerce operations, helping customers discover relevant add-on products while giving cafe administrators greater control over product relationships.