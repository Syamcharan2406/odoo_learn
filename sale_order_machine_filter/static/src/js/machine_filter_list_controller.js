/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ListController } from "@web/views/list/list_controller";

export class SaleOrderFilterController extends ListController {
    setup() {
        super.setup();
    }

    async onClickFilter(filterType) {
        const domain = [];

        if (filterType === "AC") {
            domain.push(["machine_type", "=", "aircraft"]);
        } else if (filterType === "ENG") {
            domain.push(["machine_type", "=", "engine"]);
        }

        // Apply the filter
        this.model.load({ domain });
    }
}

// Extend the sale order tree view
registry.category("views").add("sale_order_machine_filter", {
    ...registry.category("views").get("list"),
    Controller: SaleOrderFilterController,
});
