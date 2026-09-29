# Grocery Billing System

## 1. Problem Statement

In grocery stores, manually calculating the total cost of number of products can be time consuming. Maintaining product details, quantity, prices and discounts can be tedious.

The Grocery Billing System is a console based Python application that allows the user to enter the grocery product details, calculate the amount of each product, apply the discount if any and generate the final bill.

The project is aimed to showcase the core python concepts.
---

## 2. Objectives

1. Entering the grocery product details.
2. Storing the name and category of each product.
3. Entering the quantity and price of products.
4. To check whether a discount is available.
5. Calculation of the amount of each product.

6. Apply discounts where ever applicable.

7. Allow multiple grocery products to be added.

8. Calculating the final bill amount.
9. Displaying a clean and organised grocery bill.
---
## 3. Main Features

- Product Entry
- Product Category

- Quantity and Price Entry

- Discount Availability

- Discount Calculation
- Multiple Product Entry
- Individual Product Amount Calculation
- Total Bill Calculation
- Bill Generation
- Input Validation
---
## 4. Functional Requirements
### Product Management
The system will collect:
- Product name
- Category
- Quantity
- Price
- Discount availability
### Billing
The system will:
- Calculate the amount based on quantity and price.
- Check whether a discount is available.
- Apply the applicable discount.
- Calculate the final amount for each product.
- Calculate the total bill.
### Multiple Products
The system will allow the user to:
- Add a grocery product.
- Choose whether to add another product.
- Keep adding products until the user chooses to stop.
### Bill Generation
The system must display:
- Product name
- Quantity
- Price
- Discount status
- Final amount for each product
- Total bill amount
---
## 5. Input Validation
The program will ensure that:
- Product name is entered.
- Category is entered.
- Quantity is not negative.
- Price is not negative.
- Discount input is either yes or no.
- Invalid numerical input is handled correctly.
---
## 6. Technologies Used
The project is developed using Python.
Core concepts of Python such as:
- Functions
- Modules
- Lists
- Dictionaries
- Conditional Statements
- Loops
- Input Validation
- Arithmetic Operations
---
## 7. Testing
The program must be tested using valid and invalid inputs.
| Test Case | Input / Action | Expected Result |
|---|---|---|
| TC01 | Enter valid product details | Product is accepted |
| TC02 | Enter valid quantity and price | Values are accepted |
| TC03 | Enter negative quantity | Invalid value is rejected |
| TC04 | Enter negative price | Invalid value is rejected |
| TC05 | Select discount as yes | Discount is applied |
| TC06 | Select discount as no | No discount is applied |
| TC07 | Add multiple products | All products are stored |
| TC08 | Choose no when asked to add another product | Product entry stops |
| TC09 | Enter invalid numerical input | Invalid input is handled |
| TC10 | Generate bill | Final bill is displayed correctly |
---
## 8. Future Scope
The future scope of this project may include:
- Adding the GST calculation.
- Adding different discount percentages.
- Adding customer details.
- Saving the bills to a file.
- Generating the printable bills.
- Adding a graphical user interface.
- Adding database storage.
- Allowing products to be edited or removed.
---
## 9. Project Limitations

The Grocery Billing System is a basic educational grocery billing application.
The products and billing information are stored temporarily. This version does not provide the permanent database storage.
The discount calculation is based on the fixed discount rule.
---
## 10. Conclusion
The Grocery Billing System showcases the application of the core concepts of Python programming to develop a simple billing application.

The system allows the users to enter multiple grocery products, calculate the amount of each product, apply the discount where ever applicable and then generate the final grocery bill. The project makes use of functions, modules, lists, dictionaries, loops, conditional statements and input validation.