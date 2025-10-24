/** @odoo-module **/

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { ListRenderer } from "@web/views/list/list_renderer";

export class SaleOrderListController extends ListController {
    static template = "sale.SaleOrderListView";

    setup() {
        super.setup();
    }

    /**
     * Filter Sale Orders by product_type field
     */
    async filterByProductType(type) {
        const domain = [["product_type", "=", type]];
        await this.model.load({ domain });
        this.render(true);
        console.log(`📋 Filter applied: ${type}`);
    }
}

export class SaleOrderListRenderer extends ListRenderer {
    static template = "web.ListRenderer";
}

registry.category("views").add("sale_order_machine_filter", {
    ...listView,
    buttonTemplate: "sale.SaleOrderListView.Buttons",
    Controller: SaleOrderListController,
    Renderer: SaleOrderListRenderer,
});
