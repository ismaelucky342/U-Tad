public class ShoppingCart {

    // 1. **Large Class**: This class is doing too many things. It handles the cart items, calculates totals,
    // applies discounts, and prints receipts. These responsibilities should be split into separate classes.
    
    private List<Item> items;
    private double discount;

    public ShoppingCart() {
        items = new ArrayList<>();
        discount = 0.0;
    }

    // 2. **Long Method**: The method 'calculateTotal' is doing too many things at once:
    // calculating the total price, applying the discount, and checking if any items are on sale.
    public double calculateTotal() {
        double total = 0.0;

        for (Item item : items) {
            total += item.getPrice();
        }

        if (discount > 0) {
            total = total - (total * discount); // Discount calculation
        }

        // Checking for items on sale
        for (Item item : items) {
            if (item.isOnSale()) {
                total -= item.getSaleDiscount();
            }
        }

        return total;
    }

    // 3. **Duplicated Code**: The logic for calculating totals and applying discounts is repeated in the 'calculateTotal' 
    // method and other places in the class. We should avoid repeating similar logic and instead extract it into its own method.
    
    // 4. **Primitive Obsession**: The 'discount' is a primitive type (double). A better approach would be to
    // use a specialized class to represent discounts, which could provide more flexibility in the future (e.g., 
    // different types of discounts, special conditions, etc.).
    
    // 5. **Large Method**: The 'printReceipt' method does too many things. It formats the receipt, 
    // prints the item list, and calculates the final total. These responsibilities should be extracted into smaller methods.
    public void printReceipt() {
        System.out.println("Receipt:");
        for (Item item : items) {
            System.out.println(item.getName() + " - " + item.getPrice());
        }
        System.out.println("Total: " + calculateTotal());
    }

    // 6. **God Method**: The method 'addItem' handles too many responsibilities, including validating the item,
    // adding it to the list, and calculating totals.
    public void addItem(Item item) {
        if (item == null || item.getPrice() <= 0) {
            System.out.println("Invalid item");
            return;
        }
        items.add(item);
        // Recalculate total each time an item is added (should be handled elsewhere)
        System.out.println("Item added: " + item.getName());
    }
}

class Item {
    private String name;
    private double price;
    private boolean onSale;
    private double saleDiscount;

    public Item(String name, double price) {
        this.name = name;
        this.price = price;
        this.onSale = false;
        this.saleDiscount = 0.0;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public boolean isOnSale() {
        return onSale;
    }

    public double getSaleDiscount() {
        return saleDiscount;
    }

    public void setSale(boolean onSale, double saleDiscount) {
        this.onSale = onSale;
        this.saleDiscount = saleDiscount;
    }
}
