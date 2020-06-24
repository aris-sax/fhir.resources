# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import domainresource, fhirtypes


class GuidanceResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The formal response to a guidance request.
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """

    resource_type = Field("GuidanceResponse", const=True)

    dataRequirement: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="dataRequirement",
        title="Additional required data",
        description=(
            "If the evaluation could not be completed due to lack of information, "
            "or additional information would potentially result in a more accurate "
            "response, this element will a description of the data required in "
            "order to proceed with the evaluation. A subsequent request to the "
            "service should include this data."
        ),
    )

    encounter: fhirtypes.ReferenceType = Field(
        None,
        alias="encounter",
        title="Encounter during which the response was returned",
        description=(
            "The encounter during which this response was created or to which the "
            "creation of this record is tightly associated."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter"],
    )

    evaluationMessage: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="evaluationMessage",
        title="Messages resulting from the evaluation of the artifact or artifacts",
        description=(
            "Messages resulting from the evaluation of the artifact or artifacts. "
            "As part of evaluating the request, the engine may produce "
            "informational or warning messages. These messages will be provided by "
            "this element."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationOutcome"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Allows a service to provide  unique, business identifiers for the "
            "response."
        ),
    )

    moduleCanonical: fhirtypes.Canonical = Field(
        None,
        alias="moduleCanonical",
        title="What guidance was requested",
        description=(
            "An identifier, CodeableConcept or canonical reference to the guidance "
            "that was requested."
        ),
        # Choice of Data Types. i.e module[x]
        one_of_many="module",
        one_of_many_required=True,
    )
    moduleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_moduleCanonical", title="Extension field for ``moduleCanonical``."
    )

    moduleCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="moduleCodeableConcept",
        title="What guidance was requested",
        description=(
            "An identifier, CodeableConcept or canonical reference to the guidance "
            "that was requested."
        ),
        # Choice of Data Types. i.e module[x]
        one_of_many="module",
        one_of_many_required=True,
    )

    moduleUri: fhirtypes.Uri = Field(
        None,
        alias="moduleUri",
        title="What guidance was requested",
        description=(
            "An identifier, CodeableConcept or canonical reference to the guidance "
            "that was requested."
        ),
        # Choice of Data Types. i.e module[x]
        one_of_many="module",
        one_of_many_required=True,
    )
    moduleUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_moduleUri", title="Extension field for ``moduleUri``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Additional notes about the response",
        description=(
            "Provides a mechanism to communicate additional information about the "
            "response."
        ),
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the guidance response was processed",
        description="Indicates when the guidance response was processed.",
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    outputParameters: fhirtypes.ReferenceType = Field(
        None,
        alias="outputParameters",
        title="The output parameters of the evaluation, if any",
        description=(
            "The output parameters of the evaluation, if any. Many modules will "
            "result in the return of specific resources such as procedure or "
            "communication requests that are returned as part of the operation "
            "result. However, modules may define specific outputs that would be "
            "returned as the result of the evaluation, and these would be returned "
            "in this element."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Parameters"],
    )

    performer: fhirtypes.ReferenceType = Field(
        None,
        alias="performer",
        title="Device returning the guidance",
        description="Provides a reference to the device that performed the guidance.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Why guidance is needed",
        description=(
            "Describes the reason for the guidance response in coded or textual "
            "form."
        ),
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why guidance is needed",
        description=(
            "Indicates the reason the request was initiated. This is typically "
            "provided as a parameter to the evaluation and echoed by the service, "
            "although for some use cases, such as subscription- or event-based "
            "scenarios, it may provide an indication of the cause for the response."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "DiagnosticReport",
            "DocumentReference",
        ],
    )

    requestIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="requestIdentifier",
        title="The identifier of the request associated with this response, if any",
        description=(
            "The identifier of the request associated with this response. If an "
            "identifier was given as part of the request, it will be reproduced "
            "here to enable the requester to more easily identify the response in a"
            " multi-request scenario."
        ),
    )

    result: fhirtypes.ReferenceType = Field(
        None,
        alias="result",
        title="Proposed actions, if any",
        description="The actions, if any, produced by the evaluation of the artifact.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CarePlan", "RequestGroup"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "success | data-requested | data-required | in-progress | failure | "
            "entered-in-error"
        ),
        description=(
            "The status of the response. If the evaluation is completed "
            "successfully, the status will indicate success. However, in order to "
            "complete the evaluation, the engine may require more information. In "
            "this case, the status will be data-required, and the response will "
            "contain a description of the additional required information. If the "
            "evaluation completed successfully, but the engine determines that a "
            "potentially more accurate response could be provided if more data was "
            "available, the status will be data-requested, and the response will "
            "contain a description of the additional requested information."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "success",
            "data-requested",
            "data-required",
            "in-progress",
            "failure",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Patient the request was performed for",
        description="The patient for which the request was processed.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "module": ["moduleCanonical", "moduleCodeableConcept", "moduleUri"]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
