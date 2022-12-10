# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.language import Language


class UnexpectedLanguageError(pydantic.BaseModel):
    expected_language: Language = pydantic.Field(alias="expectedLanguage")
    actual_language: Language = pydantic.Field(alias="actualLanguage")

    class Partial(typing_extensions.TypedDict):
        expected_language: typing_extensions.NotRequired[Language]
        actual_language: typing_extensions.NotRequired[Language]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @UnexpectedLanguageError.Validators.root()
            def validate(values: UnexpectedLanguageError.Partial) -> UnexpectedLanguageError.Partial:
                ...

            @UnexpectedLanguageError.Validators.field("expected_language")
            def validate_expected_language(expected_language: Language, values: UnexpectedLanguageError.Partial) -> Language:
                ...

            @UnexpectedLanguageError.Validators.field("actual_language")
            def validate_actual_language(actual_language: Language, values: UnexpectedLanguageError.Partial) -> Language:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[UnexpectedLanguageError.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[UnexpectedLanguageError.Validators._RootValidator]] = []
        _expected_language_pre_validators: typing.ClassVar[
            typing.List[UnexpectedLanguageError.Validators.PreExpectedLanguageValidator]
        ] = []
        _expected_language_post_validators: typing.ClassVar[
            typing.List[UnexpectedLanguageError.Validators.ExpectedLanguageValidator]
        ] = []
        _actual_language_pre_validators: typing.ClassVar[
            typing.List[UnexpectedLanguageError.Validators.PreActualLanguageValidator]
        ] = []
        _actual_language_post_validators: typing.ClassVar[
            typing.List[UnexpectedLanguageError.Validators.ActualLanguageValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators._RootValidator], UnexpectedLanguageError.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators._PreRootValidator], UnexpectedLanguageError.Validators._PreRootValidator
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_language"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators.PreExpectedLanguageValidator],
            UnexpectedLanguageError.Validators.PreExpectedLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["expected_language"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators.ExpectedLanguageValidator],
            UnexpectedLanguageError.Validators.ExpectedLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_language"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators.PreActualLanguageValidator],
            UnexpectedLanguageError.Validators.PreActualLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["actual_language"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators.ActualLanguageValidator],
            UnexpectedLanguageError.Validators.ActualLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_language":
                    if pre:
                        cls._expected_language_pre_validators.append(validator)
                    else:
                        cls._expected_language_post_validators.append(validator)
                if field_name == "actual_language":
                    if pre:
                        cls._actual_language_pre_validators.append(validator)
                    else:
                        cls._actual_language_post_validators.append(validator)
                return validator

            return decorator

        class PreExpectedLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: UnexpectedLanguageError.Partial) -> typing.Any:
                ...

        class ExpectedLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: UnexpectedLanguageError.Partial) -> Language:
                ...

        class PreActualLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: UnexpectedLanguageError.Partial) -> typing.Any:
                ...

        class ActualLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: UnexpectedLanguageError.Partial) -> Language:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: UnexpectedLanguageError.Partial) -> UnexpectedLanguageError.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: UnexpectedLanguageError.Partial) -> UnexpectedLanguageError.Partial:
        for validator in UnexpectedLanguageError.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: UnexpectedLanguageError.Partial) -> UnexpectedLanguageError.Partial:
        for validator in UnexpectedLanguageError.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_language", pre=True)
    def _pre_validate_expected_language(cls, v: Language, values: UnexpectedLanguageError.Partial) -> Language:
        for validator in UnexpectedLanguageError.Validators._expected_language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_language", pre=False)
    def _post_validate_expected_language(cls, v: Language, values: UnexpectedLanguageError.Partial) -> Language:
        for validator in UnexpectedLanguageError.Validators._expected_language_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_language", pre=True)
    def _pre_validate_actual_language(cls, v: Language, values: UnexpectedLanguageError.Partial) -> Language:
        for validator in UnexpectedLanguageError.Validators._actual_language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_language", pre=False)
    def _post_validate_actual_language(cls, v: Language, values: UnexpectedLanguageError.Partial) -> Language:
        for validator in UnexpectedLanguageError.Validators._actual_language_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
