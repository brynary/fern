# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .lightweight_stackframe_information import LightweightStackframeInformation
from .submission_id import SubmissionId
from .traced_file import TracedFile


class RecordingResponseNotification(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    test_case_id: typing.Optional[str] = pydantic.Field(alias="testCaseId")
    line_number: int = pydantic.Field(alias="lineNumber")
    lightweight_stack_info: LightweightStackframeInformation = pydantic.Field(alias="lightweightStackInfo")
    traced_file: typing.Optional[TracedFile] = pydantic.Field(alias="tracedFile")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        test_case_id: typing_extensions.NotRequired[typing.Optional[str]]
        line_number: typing_extensions.NotRequired[int]
        lightweight_stack_info: typing_extensions.NotRequired[LightweightStackframeInformation]
        traced_file: typing_extensions.NotRequired[typing.Optional[TracedFile]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RecordingResponseNotification.Validators.root()
            def validate(values: RecordingResponseNotification.Partial) -> RecordingResponseNotification.Partial:
                ...

            @RecordingResponseNotification.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: RecordingResponseNotification.Partial) -> SubmissionId:
                ...

            @RecordingResponseNotification.Validators.field("test_case_id")
            def validate_test_case_id(test_case_id: typing.Optional[str], values: RecordingResponseNotification.Partial) -> typing.Optional[str]:
                ...

            @RecordingResponseNotification.Validators.field("line_number")
            def validate_line_number(line_number: int, values: RecordingResponseNotification.Partial) -> int:
                ...

            @RecordingResponseNotification.Validators.field("lightweight_stack_info")
            def validate_lightweight_stack_info(lightweight_stack_info: LightweightStackframeInformation, values: RecordingResponseNotification.Partial) -> LightweightStackframeInformation:
                ...

            @RecordingResponseNotification.Validators.field("traced_file")
            def validate_traced_file(traced_file: typing.Optional[TracedFile], values: RecordingResponseNotification.Partial) -> typing.Optional[TracedFile]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[RecordingResponseNotification.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[RecordingResponseNotification.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.SubmissionIdValidator]
        ] = []
        _test_case_id_pre_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.PreTestCaseIdValidator]
        ] = []
        _test_case_id_post_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.TestCaseIdValidator]
        ] = []
        _line_number_pre_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.PreLineNumberValidator]
        ] = []
        _line_number_post_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.LineNumberValidator]
        ] = []
        _lightweight_stack_info_pre_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.PreLightweightStackInfoValidator]
        ] = []
        _lightweight_stack_info_post_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.LightweightStackInfoValidator]
        ] = []
        _traced_file_pre_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.PreTracedFileValidator]
        ] = []
        _traced_file_post_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.TracedFileValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators._RootValidator],
            RecordingResponseNotification.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators._PreRootValidator],
            RecordingResponseNotification.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.PreSubmissionIdValidator],
            RecordingResponseNotification.Validators.PreSubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.SubmissionIdValidator],
            RecordingResponseNotification.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.PreTestCaseIdValidator],
            RecordingResponseNotification.Validators.PreTestCaseIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.TestCaseIdValidator],
            RecordingResponseNotification.Validators.TestCaseIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.PreLineNumberValidator],
            RecordingResponseNotification.Validators.PreLineNumberValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.LineNumberValidator],
            RecordingResponseNotification.Validators.LineNumberValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["lightweight_stack_info"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.PreLightweightStackInfoValidator],
            RecordingResponseNotification.Validators.PreLightweightStackInfoValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["lightweight_stack_info"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.LightweightStackInfoValidator],
            RecordingResponseNotification.Validators.LightweightStackInfoValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["traced_file"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.PreTracedFileValidator],
            RecordingResponseNotification.Validators.PreTracedFileValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["traced_file"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.TracedFileValidator],
            RecordingResponseNotification.Validators.TracedFileValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "test_case_id":
                    if pre:
                        cls._test_case_id_pre_validators.append(validator)
                    else:
                        cls._test_case_id_post_validators.append(validator)
                if field_name == "line_number":
                    if pre:
                        cls._line_number_pre_validators.append(validator)
                    else:
                        cls._line_number_post_validators.append(validator)
                if field_name == "lightweight_stack_info":
                    if pre:
                        cls._lightweight_stack_info_pre_validators.append(validator)
                    else:
                        cls._lightweight_stack_info_post_validators.append(validator)
                if field_name == "traced_file":
                    if pre:
                        cls._traced_file_pre_validators.append(validator)
                    else:
                        cls._traced_file_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: RecordingResponseNotification.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: RecordingResponseNotification.Partial) -> SubmissionId:
                ...

        class PreTestCaseIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: RecordingResponseNotification.Partial) -> typing.Any:
                ...

        class TestCaseIdValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: RecordingResponseNotification.Partial
            ) -> typing.Optional[str]:
                ...

        class PreLineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: RecordingResponseNotification.Partial) -> typing.Any:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: RecordingResponseNotification.Partial) -> int:
                ...

        class PreLightweightStackInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: RecordingResponseNotification.Partial) -> typing.Any:
                ...

        class LightweightStackInfoValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: LightweightStackframeInformation, __values: RecordingResponseNotification.Partial
            ) -> LightweightStackframeInformation:
                ...

        class PreTracedFileValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: RecordingResponseNotification.Partial) -> typing.Any:
                ...

        class TracedFileValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[TracedFile], __values: RecordingResponseNotification.Partial
            ) -> typing.Optional[TracedFile]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: RecordingResponseNotification.Partial
            ) -> RecordingResponseNotification.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: RecordingResponseNotification.Partial) -> RecordingResponseNotification.Partial:
        for validator in RecordingResponseNotification.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: RecordingResponseNotification.Partial) -> RecordingResponseNotification.Partial:
        for validator in RecordingResponseNotification.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(
        cls, v: SubmissionId, values: RecordingResponseNotification.Partial
    ) -> SubmissionId:
        for validator in RecordingResponseNotification.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(
        cls, v: SubmissionId, values: RecordingResponseNotification.Partial
    ) -> SubmissionId:
        for validator in RecordingResponseNotification.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id", pre=True)
    def _pre_validate_test_case_id(
        cls, v: typing.Optional[str], values: RecordingResponseNotification.Partial
    ) -> typing.Optional[str]:
        for validator in RecordingResponseNotification.Validators._test_case_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id", pre=False)
    def _post_validate_test_case_id(
        cls, v: typing.Optional[str], values: RecordingResponseNotification.Partial
    ) -> typing.Optional[str]:
        for validator in RecordingResponseNotification.Validators._test_case_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=True)
    def _pre_validate_line_number(cls, v: int, values: RecordingResponseNotification.Partial) -> int:
        for validator in RecordingResponseNotification.Validators._line_number_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=False)
    def _post_validate_line_number(cls, v: int, values: RecordingResponseNotification.Partial) -> int:
        for validator in RecordingResponseNotification.Validators._line_number_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("lightweight_stack_info", pre=True)
    def _pre_validate_lightweight_stack_info(
        cls, v: LightweightStackframeInformation, values: RecordingResponseNotification.Partial
    ) -> LightweightStackframeInformation:
        for validator in RecordingResponseNotification.Validators._lightweight_stack_info_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("lightweight_stack_info", pre=False)
    def _post_validate_lightweight_stack_info(
        cls, v: LightweightStackframeInformation, values: RecordingResponseNotification.Partial
    ) -> LightweightStackframeInformation:
        for validator in RecordingResponseNotification.Validators._lightweight_stack_info_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("traced_file", pre=True)
    def _pre_validate_traced_file(
        cls, v: typing.Optional[TracedFile], values: RecordingResponseNotification.Partial
    ) -> typing.Optional[TracedFile]:
        for validator in RecordingResponseNotification.Validators._traced_file_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("traced_file", pre=False)
    def _post_validate_traced_file(
        cls, v: typing.Optional[TracedFile], values: RecordingResponseNotification.Partial
    ) -> typing.Optional[TracedFile]:
        for validator in RecordingResponseNotification.Validators._traced_file_post_validators:
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
