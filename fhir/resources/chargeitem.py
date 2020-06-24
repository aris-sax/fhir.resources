# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItem
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ChargeItem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item containing charge code(s) associated with the provision of healthcare
    provider products.
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """

    resource_type = Field("ChargeItem", const=True)

    account: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title="Account to place this charge",
        description="Account into which this ChargeItems belongs.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    bodysite: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="bodysite",
        title="Anatomical location, if relevant",
        description="The anatomical location where the related service has been applied.",
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="A code that identifies the charge, like a billing code",
        description=None,
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter / Episode associated with event",
        description=(
            "The encounter or episode of care that establishes the context for this"
            " event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    costCenter: fhirtypes.ReferenceType = Field(
        None,
        alias="costCenter",
        title="Organization that has ownership of the (potential, future) revenue",
        description="The financial cost center permits the tracking of charge attribution.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    definitionCanonical: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="definitionCanonical",
        title="Resource defining the code of this ChargeItem",
        description=(
            "References the source of pricing information, rules of application for"
            " the code this ChargeItem uses."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItemDefinition"],
    )
    definitionCanonical__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="definitionUri",
        title="Defining information about the code of this charge item",
        description=(
            "References the (external) source of pricing information, rules of "
            "application for the code this ChargeItem uses."
        ),
    )
    definitionUri__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_definitionUri", title="Extension field for ``definitionUri``."
    )

    enteredDate: fhirtypes.DateTime = Field(
        None,
        alias="enteredDate",
        title="Date the charge item was entered",
        description=None,
    )
    enteredDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_enteredDate", title="Extension field for ``enteredDate``."
    )

    enterer: fhirtypes.ReferenceType = Field(
        None,
        alias="enterer",
        title="Individual who was entering",
        description="The device, practitioner, etc. who entered the charge item.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    factorOverride: fhirtypes.Decimal = Field(
        None,
        alias="factorOverride",
        title="Factor overriding the associated rules",
        description=(
            "Factor overriding the factor determined by the rules associated with "
            "the code."
        ),
    )
    factorOverride__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factorOverride", title="Extension field for ``factorOverride``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for item",
        description="Identifiers assigned to this event performer or other systems.",
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the ChargeItem",
        description=(
            "Comments made about the event by the performer, subject or other "
            "participants."
        ),
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="occurrencePeriod",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When the charged service was applied",
        description="Date/time(s) or duration when the charged service was applied.",
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    overrideReason: fhirtypes.String = Field(
        None,
        alias="overrideReason",
        title="Reason for overriding the list price/factor",
        description=(
            "If the list price or the rule-based factor associated with the code is"
            " overridden, this attribute can capture a text to indicate the  reason"
            " for this action."
        ),
    )
    overrideReason__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_overrideReason", title="Extension field for ``overrideReason``."
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced ChargeItem",
        description=(
            "ChargeItems can be grouped to larger ChargeItems covering the whole "
            "set."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItem"],
    )

    performer: ListType[fhirtypes.ChargeItemPerformerType] = Field(
        None,
        alias="performer",
        title="Who performed charged service",
        description=(
            "Indicates who or what performed or participated in the charged " "service."
        ),
    )

    performingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="performingOrganization",
        title="Organization providing the charged service",
        description="The organization requesting the service.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    priceOverride: fhirtypes.MoneyType = Field(
        None,
        alias="priceOverride",
        title="Price overriding the associated rules",
        description=(
            "Total price of the charge overriding the list price associated with "
            "the code."
        ),
    )

    productCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCodeableConcept",
        title="Product charged",
        description=(
            "Identifies the device, food, drug or other product being charged "
            "either by type code or reference to an instance."
        ),
        # Choice of Data Types. i.e product[x]
        one_of_many="product",
        one_of_many_required=False,
    )

    productReference: fhirtypes.ReferenceType = Field(
        None,
        alias="productReference",
        title="Product charged",
        description=(
            "Identifies the device, food, drug or other product being charged "
            "either by type code or reference to an instance."
        ),
        # Choice of Data Types. i.e product[x]
        one_of_many="product",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device", "Medication", "Substance"],
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Quantity of which the charge item has been serviced",
        description=None,
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why was the charged  service rendered?",
        description="Describes why the event occurred in coded or textual form.",
    )

    requestingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestingOrganization",
        title="Organization requesting the charged service",
        description="The organization performing the service.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    service: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="service",
        title="Which rendered service is being charged?",
        description="Indicated the rendered service that caused this charge.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "DiagnosticReport",
            "ImagingStudy",
            "Immunization",
            "MedicationAdministration",
            "MedicationDispense",
            "Observation",
            "Procedure",
            "SupplyDelivery",
        ],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "planned | billable | not-billable | aborted | billed | entered-in-"
            "error | unknown"
        ),
        description="The current state of the ChargeItem.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "billable",
            "not-billable",
            "aborted",
            "billed",
            "entered-in-error",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Individual service was done for/to",
        description=(
            "The individual or set of individuals the action is being or was "
            "performed on."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Further information supporting this charge",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
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
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
            "product": ["productCodeableConcept", "productReference"],
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


class ChargeItemPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed charged service.
    Indicates who or what performed or participated in the charged service.
    """

    resource_type = Field("ChargeItemPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed or participated in the "
            "service."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "PractitionerRole",
            "Organization",
            "CareTeam",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    function: fhirtypes.CodeableConceptType = Field(
        None,
        alias="function",
        title="What type of performance was done",
        description=(
            "Describes the type of performance or participation(e.g. primary "
            "surgeon, anesthesiologiest, etc.)."
        ),
    )
