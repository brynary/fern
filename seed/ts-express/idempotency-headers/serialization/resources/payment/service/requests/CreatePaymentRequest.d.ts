/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../..";
import * as SeedIdempotencyHeaders from "../../../../../api";
import * as core from "../../../../../core";
export declare const CreatePaymentRequest: core.serialization.Schema<serializers.CreatePaymentRequest.Raw, SeedIdempotencyHeaders.CreatePaymentRequest>;
export declare namespace CreatePaymentRequest {
    interface Raw {
        amount: number;
        currency: serializers.Currency.Raw;
    }
}