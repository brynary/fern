/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const WebhookGroupId: core.serialization.Schema<serializers.WebhookGroupId.Raw, FernIr.WebhookGroupId> =
    core.serialization.string();

export declare namespace WebhookGroupId {
    type Raw = string;
}