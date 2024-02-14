/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "..";
import * as SeedExtends from "../../api";
import * as core from "../../core";

export const Docs: core.serialization.ObjectSchema<serializers.Docs.Raw, SeedExtends.Docs> = core.serialization.object({
    docs: core.serialization.string(),
});

export declare namespace Docs {
    interface Raw {
        docs: string;
    }
}