/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { ListRenderer } from "@web/views/list/list_renderer";

export class SaleOrderListController extends ListController {
    static template = "sale.SaleOrderListView";

    setup() {
        super.setup();
        this.orm = useService("orm");
        this.action = useService("action");
    }

    async onDebugClick() {
        const records = this.model.root.selection;
        console.log("🔍 Selected Records:", records);
        console.log("📦 Props:", this.props);
        console.log("🧩 Model:", this.model);
        console.log("⚙️ Action Service:", this.action);
    }
}

export class SaleOrderListRenderer extends ListRenderer {
    static template = "web.ListRenderer";
}

/**
 * Register custom view
 */
registry.category("views").add("sale_order_machine_filter", {
    ...listView,
    buttonTemplate: "sale.SaleOrderListView.Buttons",
    Controller: SaleOrderListController,
    Renderer: SaleOrderListRenderer,
});
