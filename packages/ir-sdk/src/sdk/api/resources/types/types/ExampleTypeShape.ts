/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../..";

export type ExampleTypeShape =
    | FernIr.ExampleTypeShape.Alias
    | FernIr.ExampleTypeShape.Enum
    | FernIr.ExampleTypeShape.Object_
    | FernIr.ExampleTypeShape.Union
    | FernIr.ExampleTypeShape.UndiscriminatedUnion;

export declare namespace ExampleTypeShape {
    interface Alias extends FernIr.ExampleAliasType, _Utils {
        type: "alias";
    }

    interface Enum extends FernIr.ExampleEnumType, _Utils {
        type: "enum";
    }

    interface Object_ extends FernIr.ExampleObjectType, _Utils {
        type: "object";
    }

    interface Union extends FernIr.ExampleUnionType, _Utils {
        type: "union";
    }

    interface UndiscriminatedUnion extends FernIr.ExampleUndiscriminatedUnionType, _Utils {
        type: "undiscriminatedUnion";
    }

    interface _Utils {
        _visit: <_Result>(visitor: FernIr.ExampleTypeShape._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        alias: (value: FernIr.ExampleAliasType) => _Result;
        enum: (value: FernIr.ExampleEnumType) => _Result;
        object: (value: FernIr.ExampleObjectType) => _Result;
        union: (value: FernIr.ExampleUnionType) => _Result;
        undiscriminatedUnion: (value: FernIr.ExampleUndiscriminatedUnionType) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const ExampleTypeShape = {
    alias: (value: FernIr.ExampleAliasType): FernIr.ExampleTypeShape.Alias => {
        return {
            ...value,
            type: "alias",
            _visit: function <_Result>(
                this: FernIr.ExampleTypeShape.Alias,
                visitor: FernIr.ExampleTypeShape._Visitor<_Result>
            ) {
                return FernIr.ExampleTypeShape._visit(this, visitor);
            },
        };
    },

    enum: (value: FernIr.ExampleEnumType): FernIr.ExampleTypeShape.Enum => {
        return {
            ...value,
            type: "enum",
            _visit: function <_Result>(
                this: FernIr.ExampleTypeShape.Enum,
                visitor: FernIr.ExampleTypeShape._Visitor<_Result>
            ) {
                return FernIr.ExampleTypeShape._visit(this, visitor);
            },
        };
    },

    object: (value: FernIr.ExampleObjectType): FernIr.ExampleTypeShape.Object_ => {
        return {
            ...value,
            type: "object",
            _visit: function <_Result>(
                this: FernIr.ExampleTypeShape.Object_,
                visitor: FernIr.ExampleTypeShape._Visitor<_Result>
            ) {
                return FernIr.ExampleTypeShape._visit(this, visitor);
            },
        };
    },

    union: (value: FernIr.ExampleUnionType): FernIr.ExampleTypeShape.Union => {
        return {
            ...value,
            type: "union",
            _visit: function <_Result>(
                this: FernIr.ExampleTypeShape.Union,
                visitor: FernIr.ExampleTypeShape._Visitor<_Result>
            ) {
                return FernIr.ExampleTypeShape._visit(this, visitor);
            },
        };
    },

    undiscriminatedUnion: (
        value: FernIr.ExampleUndiscriminatedUnionType
    ): FernIr.ExampleTypeShape.UndiscriminatedUnion => {
        return {
            ...value,
            type: "undiscriminatedUnion",
            _visit: function <_Result>(
                this: FernIr.ExampleTypeShape.UndiscriminatedUnion,
                visitor: FernIr.ExampleTypeShape._Visitor<_Result>
            ) {
                return FernIr.ExampleTypeShape._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(value: FernIr.ExampleTypeShape, visitor: FernIr.ExampleTypeShape._Visitor<_Result>): _Result => {
        switch (value.type) {
            case "alias":
                return visitor.alias(value);
            case "enum":
                return visitor.enum(value);
            case "object":
                return visitor.object(value);
            case "union":
                return visitor.union(value);
            case "undiscriminatedUnion":
                return visitor.undiscriminatedUnion(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;