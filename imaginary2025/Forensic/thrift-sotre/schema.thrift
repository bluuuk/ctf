/**
 * Represents a product available in the inventory.
 */
struct Product {
    1: required string id,          // e.g., "apple-red-delicious"
    2: required string name,        // e.g., "Red Delicious Apple"
    3: required i64 price,          // e.g., 120 for $1.20
    4: optional string description,  // This field may not be present
}

struct BasketItem {
    1: required string id,          // e.g., "apple-red-delicious"
    2: required i8 amount,           // e.g., 120
}

struct BasketId{
    1: required string basketId,
}

struct Inventory{
    1: required list<Product> items,
}

struct BasketItems{
    1: list<BasketItem> items,
}

/**
 * Exception thrown when a payment fails.
 */
exception PaymentException {
    1: string message
}

/**
 * Defines the contract for the shopping service.
 */
service ShoppingService {
    /**
     * Retrieves the list of all available products. -> YES
     */
    Inventory getInventory(),

    /**
     * Creates a new, empty shopping basket.
     * Returns the unique ID for the new basket. -> YES
     */
    BasketId createBasket(),

    /**
     * Adds a specified product to a basket. -> ???
     */
    void addToBasket(1: string basketId, 2: string productId), 

    /**
     * Retrieves the list of product IDs currently in a basket.
     * -> NO
     *BasketItems getBasket(1: BasketId basketId),
     */
    BasketItems getBasket(1: string basketId),

    /**
     * Processes payment for the items in a given basket.
     * @throws PaymentException if the payment fails.
     */
    void pay(1: string basketId, 2: i64 amount) throws (1: PaymentException e)
}