/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../core";
import * as serializers from "../../..";
import * as SeedUnions from "../../../../api";
export declare const Shape: core.serialization.Schema<serializers.Shape.Raw, SeedUnions.Shape>;
export declare namespace Shape {
    type Raw = Shape.Circle | Shape.Square;
    interface Circle extends _Base, serializers.Circle.Raw {
        type: "circle";
    }
    interface Square extends _Base, serializers.Square.Raw {
        type: "square";
    }
    interface _Base {
        id: string;
    }
}