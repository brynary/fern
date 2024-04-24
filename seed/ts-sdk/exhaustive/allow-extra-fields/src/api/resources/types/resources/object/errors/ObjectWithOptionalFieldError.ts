/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as errors from "../../../../../../errors/index";
import * as SeedExhaustive from "../../../../../index";

export class ObjectWithOptionalFieldError extends errors.SeedExhaustiveError {
    constructor(body: SeedExhaustive.types.ObjectWithOptionalField) {
        super({
            message: "ObjectWithOptionalFieldError",
            statusCode: 400,
            body: body,
        });
        Object.setPrototypeOf(this, ObjectWithOptionalFieldError.prototype);
    }
}