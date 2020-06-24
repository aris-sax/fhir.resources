# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationDispense(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dispensing a medication to a named patient.
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    resource_type = Field("MedicationDispense", const=True)

    authorizingPrescription: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="authorizingPrescription",
        title="Medication order that authorizes the dispense",
        description="Indicates the medication order that is being dispensed against.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of medication dispense",
        description=(
            "Indicates type of medication dispense and where the medication is "
            "expected to be consumed or administered."
        ),
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

    daysSupply: fhirtypes.QuantityType = Field(
        None,
        alias="daysSupply",
        title="Amount of medication expressed as a timing amount",
        description="The amount of medication expressed as a timing amount.",
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Where the medication was sent",
        description=(
            "Identification of the facility/location where the medication was "
            "shipped to, as part of the dispense event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    detectedIssue: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="detectedIssue",
        title="Clinical issue with action",
        description=(
            "Indicates an actual or potential clinical issue with or between one or"
            " more active or proposed clinical actions for a patient; e.g. Drug-"
            "drug interaction, duplicate therapy, dosage alert etc."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DetectedIssue"],
    )

    dosageInstruction: ListType[fhirtypes.DosageType] = Field(
        None,
        alias="dosageInstruction",
        title=(
            "How the medication is to be used by the patient or administered by the"
            " caregiver"
        ),
        description="Indicates how the medication is to be used by the patient.",
    )

    eventHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title="A list of releveant lifecycle events",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the dispense was verified."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier assigned by the dispensing facility - this is an identifier"
            " assigned outside FHIR."
        ),
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="What medication was supplied",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
    )

    medicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="medicationReference",
        title="What medication was supplied",
        description=(
            "Identifies the medication being administered. This is either a link to"
            " a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    notDone: bool = Field(
        None,
        alias="notDone",
        title="Whether the dispense was or was not performed",
        description="True if the dispense was not performed for some reason.",
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReasonCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notDoneReasonCodeableConcept",
        title="Why a dispense was not performed",
        description="Indicates the reason why a dispense was not performed.",
        # Choice of Data Types. i.e notDoneReason[x]
        one_of_many="notDoneReason",
        one_of_many_required=False,
    )

    notDoneReasonReference: fhirtypes.ReferenceType = Field(
        None,
        alias="notDoneReasonReference",
        title="Why a dispense was not performed",
        description="Indicates the reason why a dispense was not performed.",
        # Choice of Data Types. i.e notDoneReason[x]
        one_of_many="notDoneReason",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DetectedIssue"],
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Information about the dispense",
        description=(
            "Extra information about the dispense that could not be conveyed in the"
            " other attributes."
        ),
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Event that dispense is part of",
        description="The procedure that the dispense is done because of.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Procedure"],
    )

    performer: ListType[fhirtypes.MedicationDispensePerformerType] = Field(
        None,
        alias="performer",
        title="Who performed event",
        description=(
            "Indicates who or what performed the event.  It should be assumed that "
            "the performer is the dispenser of the medication."
        ),
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Amount dispensed",
        description=(
            "The amount of medication that has been dispensed. Includes unit of "
            "measure."
        ),
    )

    receiver: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="receiver",
        title="Who collected the medication",
        description=(
            "Identifies the person who picked up the medication.  This will usually"
            " be a patient or their caregiver, but some cases exist where it can be"
            " a healthcare professional."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title=(
            "preparation | in-progress | on-hold | completed | entered-in-error | "
            "stopped"
        ),
        description="A code specifying the state of the set of dispense events.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Who the dispense is for",
        description=(
            "A link to a resource representing the person or the group to whom the "
            "medication will be given."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    substitution: fhirtypes.MedicationDispenseSubstitutionType = Field(
        None,
        alias="substitution",
        title="Whether a substitution was performed on the dispense",
        description=(
            "Indicates whether or not substitution was made as part of the "
            "dispense.  In some cases substitution will be expected but does not "
            "happen, in other cases substitution is not expected but does happen.  "
            "This block explains what substitution did or did not happen and why.  "
            "If nothing is specified, substitution was not done."
        ),
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Information that supports the dispensing of the medication",
        description="Additional information that supports the medication being dispensed.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Trial fill, partial fill, emergency fill, etc.",
        description=(
            "Indicates the type of dispensing event that is performed. For example,"
            " Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, "
            "Samples, etc."
        ),
    )

    whenHandedOver: fhirtypes.DateTime = Field(
        None,
        alias="whenHandedOver",
        title="When product was given out",
        description=(
            "The time the dispensed product was provided to the patient or their "
            "representative."
        ),
    )
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whenHandedOver", title="Extension field for ``whenHandedOver``."
    )

    whenPrepared: fhirtypes.DateTime = Field(
        None,
        alias="whenPrepared",
        title="When product was packaged and reviewed",
        description="The time when the dispensed product was packaged and reviewed.",
    )
    whenPrepared__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whenPrepared", title="Extension field for ``whenPrepared``."
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
            "medication": ["medicationCodeableConcept", "medicationReference"],
            "notDoneReason": ["notDoneReasonCodeableConcept", "notDoneReasonReference"],
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


class MedicationDispensePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who or what performed the event.  It should be assumed that the
    performer is the dispenser of the medication.
    """

    resource_type = Field("MedicationDispensePerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed the action.  It should be"
            " assumed that the actor is the dispenser of the medication."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Practitioner",
            "Organization",
            "Patient",
            "Device",
            "RelatedPerson",
        ],
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization organization was acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether a substitution was performed on the dispense.
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    resource_type = Field("MedicationDispenseSubstitution", const=True)

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why was substitution made",
        description=(
            "Indicates the reason for the substitution of (or lack of substitution)"
            " from what was prescribed."
        ),
    )

    responsibleParty: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="responsibleParty",
        title="Who is responsible for the substitution",
        description=(
            "The person or organization that has primary responsibility for the "
            "substitution."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title=(
            "Code signifying whether a different drug was dispensed from what was "
            "prescribed"
        ),
        description=(
            "A code signifying whether a different drug was dispensed from what was"
            " prescribed."
        ),
    )

    wasSubstituted: bool = Field(
        ...,
        alias="wasSubstituted",
        title="Whether a substitution was or was not performed on the dispense",
        description=(
            "True if the dispenser dispensed a different drug or product from what "
            "was prescribed."
        ),
    )
    wasSubstituted__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_wasSubstituted", title="Extension field for ``wasSubstituted``."
    )
