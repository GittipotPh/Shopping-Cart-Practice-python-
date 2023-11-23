import sys

class ShoppingCart:

    def __init__(self):
        self.items = []
        self.points = 0
        self.remainpoints = 0
        self.points_used = 0

    def add_item(self, name, price):
        item = (name, price)
        self.items.append(item)
        
 
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
    def Couponfixed(self):
        total = self.calculate_total()
        return total - 50
    
    def CouponPercentage(self):
        total = self.calculate_total()
        Percentagediscount = total * 0.1
        return total - Percentagediscount
    
    def Ontop_Category(self, category_items):  
        Clothing = ["T-shirt", "Hoodie"]
        
        total = 0

        for item in self.items:
            name, price = item
            if name in Clothing:
                total += price * 0.85
        
            else:
                total += price

        return total

    def Ontop_Points(self):

        if sys.stdin.isatty():

            Currentpoints = int(input("Please in put your remaining point:",))
            print(" ")
            Point_to_use = int(input("How many point do you want to use:"))
            print(" ")

        else:
       
            Currentpoints = 0
        
        self.points += Currentpoints
        self.remainpoints = Currentpoints - Point_to_use
        self.points_used = Point_to_use
        total = self.calculate_total()
        Maximum_discount = total*0.2
        
        if Point_to_use > 0 and self.remainpoints >= 0:
            if Point_to_use >= Maximum_discount:
                return total - Maximum_discount
            elif Point_to_use < Maximum_discount:
                return total - Point_to_use
        else:
            self.points = Currentpoints
            self.remainpoints = Currentpoints
            self.points_used = 0
            return total
        
    def Seasonnal(self):
        total = self.calculate_total()
        discount_amount = (total // 300) * 40
        return total - discount_amount

def main():

    cart = ShoppingCart()

    cart.add_item("T-shirt", 350)
    cart.add_item("Hoodie", 700)
    cart.add_item("Bag", 640)
    cart.add_item("Watch", 850)

    print("Current Items in Cart:")
    for item in cart.items:
        print(item[0], "-", item[1])

    Total_price = cart.calculate_total()
    print("Total Price:",Total_price, "\n")
    

    DiscountFixedCoupon = cart.Couponfixed()
    print("Total Price after deduction by Fixed Coupon:", DiscountFixedCoupon , "\n")

    DiscountPercentage = cart.CouponPercentage()
    print("Total Price after deduction by Percentage Coupon:", DiscountPercentage, "\n")
    
    category_items = ["T-shirt", "Hoodie"]
    DiscountCategory = cart.Ontop_Category(category_items)
    print("Total Price after deduction by Categoey:", DiscountCategory, "\n")

    DiscountOnTopPoints = cart.Ontop_Points()
    print("Total price after deduction by Points:", DiscountOnTopPoints)
    print("Remaining points:", cart.remainpoints)
    print("Point used:", cart.points_used, "\n")

    DiscountonSeasonal = cart.Seasonnal()
    print("Total Price after deduction by Seasonal:", DiscountonSeasonal)


if __name__ == "__main__":
    main()