/** @odoo-module **/

import { Interaction } from "@web/public/interaction";

export class ProductAccessoriesInteraction extends Interaction {
    static selector = "#product_accessories";

    events = {
        "click #add_to_cart_with_accessories": this.addWithAccessories,
        "change .accessory-checkbox": this.toggleCard,
    };

    toggleCard(event) {
        const checkbox = event.currentTarget;
        const card = checkbox.closest(".product_accessory_card");
        if (card) {
            card.classList.toggle("is-selected", checkbox.checked);
        }
    }

    async addWithAccessories() {
        const productIdInput = document.querySelector(
            "#product_detail input[name='product_id'], #product_detail input.product_id"
        );
        const productId = productIdInput?.value;

        if (!productId || productId === "0") {
            window.alert("Please select a product variant first.");
            return;
        }

        const button = document.querySelector("#add_to_cart_with_accessories");
        const accessoryIds = Array.from(
            document.querySelectorAll("#product_accessories .accessory-checkbox:checked")
        ).map((input) => input.value);

        const formData = new FormData();
        formData.append("product_id", productId);
        for (const accessoryId of accessoryIds) {
            formData.append("accessory_ids", accessoryId);
        }

        const csrfToken = document.querySelector("input[name='csrf_token']")?.value;
        if (csrfToken) {
            formData.append("csrf_token", csrfToken);
        }

        const originalHtml = button.innerHTML;
        button.disabled = true;
        button.innerHTML = '<i class="fa fa-spinner fa-spin me-1"></i> Adding...';

        try {
            const response = await fetch("/shop/product/add_with_accessories", {
                method: "POST",
                body: formData,
                credentials: "same-origin",
            });

            if (!response.ok) {
                throw new Error("Unable to add products to the cart.");
            }

            window.location.href = response.url || "/shop/cart";
        } catch (error) {
            console.error(error);
            button.disabled = false;
            button.innerHTML = originalHtml;
            window.alert("Could not add the product and accessories. Please try again.");
        }
    }
}

export default ProductAccessoriesInteraction;
