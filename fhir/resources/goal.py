# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Goal
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Goal(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes the intended objective(s) for a patient, group or organization.
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = Field("Goal", const=True)

    achievementStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="achievementStatus",
        title=(
            "in-progress | improving | worsening | no-change | achieved | "
            "sustaining | not-achieved | no-progress | not-attainable"
        ),
        description=(
            "Describes the progression, or lack thereof, towards the goal against "
            "the target."
        ),
    )

    addresses: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="addresses",
        title="Issues addressed by this goal",
        description=(
            "The identified conditions and other health record elements that are "
            "intended to be addressed by the goal."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Condition",
            "Observation",
            "MedicationStatement",
            "NutritionOrder",
            "ServiceRequest",
            "RiskAssessment",
        ],
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="E.g. Treatment, dietary, behavioral, etc.",
        description="Indicates a category the goal falls within.",
    )

    description: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="description",
        title="Code or text describing goal",
        description=(
            "Human-readable and/or coded description of a specific desired "
            'objective of care, such as "control blood pressure" or "negotiate an '
            'obstacle course" or "dance with child at wedding".'
        ),
    )

    expressedBy: fhirtypes.ReferenceType = Field(
        None,
        alias="expressedBy",
        title="Who's responsible for creating Goal?",
        description="Indicates whose goal this is - patient goal, practitioner goal, etc.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
        ],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External Ids for this goal",
        description=(
            "Business identifiers assigned to this goal by the performer or other "
            "systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
    )

    lifecycleStatus: fhirtypes.Code = Field(
        ...,
        alias="lifecycleStatus",
        title=(
            "proposed | planned | accepted | active | on-hold | completed | "
            "cancelled | entered-in-error | rejected"
        ),
        description="The state of the goal throughout its lifecycle.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "proposed",
            "planned",
            "accepted",
            "active",
            "on-hold",
            "completed",
            "cancelled",
            "entered-in-error",
            "rejected",
        ],
    )
    lifecycleStatus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lifecycleStatus", title="Extension field for ``lifecycleStatus``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments about the goal",
        description="Any comments related to the goal.",
    )

    outcomeCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="outcomeCode",
        title="What result was achieved regarding the goal?",
        description=(
            "Identifies the change (or lack of change) at the point when the status"
            " of the goal is assessed."
        ),
    )

    outcomeReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="outcomeReference",
        title="Observation that resulted from goal",
        description="Details of what's changed (or not changed).",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Observation"],
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="high-priority | medium-priority | low-priority",
        description=(
            "Identifies the mutually agreed level of importance associated with "
            "reaching/sustaining the goal."
        ),
    )

    startCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="startCodeableConcept",
        title="When goal pursuit begins",
        description="The date or event after which the goal should begin being pursued.",
        # Choice of Data Types. i.e start[x]
        one_of_many="start",
        one_of_many_required=False,
    )

    startDate: fhirtypes.Date = Field(
        None,
        alias="startDate",
        title="When goal pursuit begins",
        description="The date or event after which the goal should begin being pursued.",
        # Choice of Data Types. i.e start[x]
        one_of_many="start",
        one_of_many_required=False,
    )
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_startDate", title="Extension field for ``startDate``."
    )

    statusDate: fhirtypes.Date = Field(
        None,
        alias="statusDate",
        title="When goal status took effect",
        description=(
            "Identifies when the current status.  I.e. When initially created, when"
            " achieved, when cancelled, etc."
        ),
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    statusReason: fhirtypes.String = Field(
        None,
        alias="statusReason",
        title="Reason for current status",
        description="Captures the reason for the current status.",
    )
    statusReason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusReason", title="Extension field for ``statusReason``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who this goal is intended for",
        description=(
            "Identifies the patient, group or organization for whom the goal is "
            "being established."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group", "Organization"],
    )

    target: ListType[fhirtypes.GoalTargetType] = Field(
        None,
        alias="target",
        title="Target outcome for the goal",
        description="Indicates what should be done by when.",
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
        one_of_many_fields = {"start": ["startCodeableConcept", "startDate"]}
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


class GoalTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target outcome for the goal.
    Indicates what should be done by when.
    """

    resource_type = Field("GoalTarget", const=True)

    detailBoolean: bool = Field(
        None,
        alias="detailBoolean",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )
    detailBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailBoolean", title="Extension field for ``detailBoolean``."
    )

    detailCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="detailCodeableConcept",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailInteger: fhirtypes.Integer = Field(
        None,
        alias="detailInteger",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )
    detailInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailInteger", title="Extension field for ``detailInteger``."
    )

    detailQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="detailQuantity",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailRange: fhirtypes.RangeType = Field(
        None,
        alias="detailRange",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailRatio: fhirtypes.RatioType = Field(
        None,
        alias="detailRatio",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailString: fhirtypes.String = Field(
        None,
        alias="detailString",
        title="The target value to be achieved",
        description=(
            "The target value of the focus to be achieved to signify the "
            "fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low"
            " or both values of the range can be specified. When a low value is "
            "missing, it indicates that the goal is achieved at any focus value at "
            "or below the high value. Similarly, if the high value is missing, it "
            "indicates that the goal is achieved at any focus value at or above the"
            " low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )
    detailString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailString", title="Extension field for ``detailString``."
    )

    dueDate: fhirtypes.Date = Field(
        None,
        alias="dueDate",
        title="Reach goal on or before",
        description=(
            "Indicates either the date or the duration after start by which the "
            "goal should be met."
        ),
        # Choice of Data Types. i.e due[x]
        one_of_many="due",
        one_of_many_required=False,
    )
    dueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dueDate", title="Extension field for ``dueDate``."
    )

    dueDuration: fhirtypes.DurationType = Field(
        None,
        alias="dueDuration",
        title="Reach goal on or before",
        description=(
            "Indicates either the date or the duration after start by which the "
            "goal should be met."
        ),
        # Choice of Data Types. i.e due[x]
        one_of_many="due",
        one_of_many_required=False,
    )

    measure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="measure",
        title="The parameter whose value is being tracked",
        description=(
            "The parameter whose value is being tracked, e.g. body weight, blood "
            "pressure, or hemoglobin A1c level."
        ),
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
            "detail": [
                "detailBoolean",
                "detailCodeableConcept",
                "detailInteger",
                "detailQuantity",
                "detailRange",
                "detailRatio",
                "detailString",
            ],
            "due": ["dueDate", "dueDuration"],
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
