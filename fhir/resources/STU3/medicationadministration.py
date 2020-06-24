# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class MedicationAdministration(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Administration of medication to a patient.
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    resource_type = Field("MedicationAdministration", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Type of medication usage",
        description=(
            "Indicates the type of medication administration and where the "
            "medication is expected to be consumed or administered."
        ),
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter or Episode of Care administered as part of",
        description=(
            "The visit, admission or other contact between patient and health care "
            "provider the medication administration was performed as part of."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    definition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol, guideline, orderset or other definition that was adhered "
            "to in whole or in part by this event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PlanDefinition", "ActivityDefinition"],
    )

    device: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="device",
        title="Device used to administer",
        description=(
            "The device used in administering the medication to the patient.  For "
            "example, a particular infusion pump."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    dosage: fhirtypes.MedicationAdministrationDosageType = Field(
        None,
        alias="dosage",
        title="Details of how medication was taken",
        description=(
            "Describes the medication dosage information details e.g. dose, rate, "
            "site, route, etc."
        ),
    )

    effectiveDateTime: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDateTime",
        title="Start and end time of administration",
        description=(
            "A specific date/time or interval of time during which the "
            "administration took place (or did not take place, when the 'notGiven' "
            "attribute is true). For many administrations, such as swallowing a "
            "tablet the use of dateTime is more appropriate."
        ),
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=True,
    )
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_effectiveDateTime",
        title="Extension field for ``effectiveDateTime``.",
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="Start and end time of administration",
        description=(
            "A specific date/time or interval of time during which the "
            "administration took place (or did not take place, when the 'notGiven' "
            "attribute is true). For many administrations, such as swallowing a "
            "tablet the use of dateTime is more appropriate."
        ),
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=True,
    )

    eventHistory: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="eventHistory",
        title="A list of events of interest in the lifecycle",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the administration was verified."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Provenance"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "External identifier - FHIR will generate its own internal identifiers "
            "(probably URLs) which do not need to be explicitly managed by the "
            "resource.  The identifier here is one that would be used by another "
            "non-FHIR system - for example an automated medication pump would "
            "provide a record each time it operated; an administration while the "
            "patient was off the ward might be made with a different system and "
            "entered after the event.  Particularly important if these records have"
            " to be updated."
        ),
    )

    medicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="medicationCodeableConcept",
        title="What was administered",
        description=(
            "Identifies the medication that was administered. This is either a link"
            " to a resource representing the details of the medication or a simple "
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
        title="What was administered",
        description=(
            "Identifies the medication that was administered. This is either a link"
            " to a resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        # Choice of Data Types. i.e medication[x]
        one_of_many="medication",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication"],
    )

    notGiven: bool = Field(
        None,
        alias="notGiven",
        title="True if medication not administered",
        description=(
            "Set this to true if the record is saying that the medication was NOT "
            "administered."
        ),
    )
    notGiven__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notGiven", title="Extension field for ``notGiven``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Information about the administration",
        description=(
            "Extra information about the medication administration that is not "
            "conveyed by the other attributes."
        ),
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationAdministration", "Procedure"],
    )

    performer: ListType[fhirtypes.MedicationAdministrationPerformerType] = Field(
        None,
        alias="performer",
        title="Who administered substance",
        description=(
            "The individual who was responsible for giving the medication to the "
            "patient."
        ),
    )

    prescription: fhirtypes.ReferenceType = Field(
        None,
        alias="prescription",
        title="Request administration performed against",
        description=(
            "The original request, instruction or authority to perform the "
            "administration."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicationRequest"],
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Reason administration performed",
        description="A code indicating why the medication was given.",
    )

    reasonNotGiven: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonNotGiven",
        title="Reason administration not performed",
        description="A code indicating why the administration was not performed.",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "Condition or Observation that supports why the medication was "
            "administered"
        ),
        description=(
            "Condition or observation that supports why the medication was "
            "administered."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "in-progress | on-hold | completed | entered-in-error | stopped | "
            "unknown"
        ),
        description=(
            "Will generally be set to show that the administration has been "
            "completed.  For some long running administrations such as infusions it"
            " is possible for an administration to be started but not completed or "
            "it may be paused while some other process is under way."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "in-progress",
            "on-hold",
            "completed",
            "entered-in-error",
            "stopped",
            "unknown",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who received medication",
        description="The person or animal or group receiving the medication.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    supportingInformation: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="supportingInformation",
        title="Additional information to support administration",
        description=(
            "Additional information (for example, patient height and weight) that "
            "supports the administration of the medication."
        ),
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
            "effective": ["effectiveDateTime", "effectivePeriod"],
            "medication": ["medicationCodeableConcept", "medicationReference"],
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


class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details of how medication was taken.
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """

    resource_type = Field("MedicationAdministrationDosage", const=True)

    dose: fhirtypes.QuantityType = Field(
        None,
        alias="dose",
        title="Amount of medication per dose",
        description=(
            "The amount of the medication given at one administration event.   Use "
            "this value when the administration is essentially an instantaneous "
            "event such as a swallowing a tablet or giving an injection."
        ),
    )

    method: fhirtypes.CodeableConceptType = Field(
        None,
        alias="method",
        title="How drug was administered",
        description=(
            "A coded value indicating the method by which the medication is "
            "intended to be or was introduced into or on the body.  This attribute "
            "will most often NOT be populated.  It is most commonly used for "
            "injections.  For example, Slow Push, Deep IV."
        ),
    )

    rateQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="rateQuantity",
        title="Dose quantity per unit of time",
        description=(
            "Identifies the speed with which the medication was or will be "
            "introduced into the patient.  Typically the rate for an infusion e.g. "
            "100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate per "
            "unit of time e.g. 500 ml per 2 hours.  Other examples:  200 mcg/min or"
            " 200 mcg/1 minute; 1 liter/8 hours."
        ),
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    rateRatio: fhirtypes.RatioType = Field(
        None,
        alias="rateRatio",
        title="Dose quantity per unit of time",
        description=(
            "Identifies the speed with which the medication was or will be "
            "introduced into the patient.  Typically the rate for an infusion e.g. "
            "100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate per "
            "unit of time e.g. 500 ml per 2 hours.  Other examples:  200 mcg/min or"
            " 200 mcg/1 minute; 1 liter/8 hours."
        ),
        # Choice of Data Types. i.e rate[x]
        one_of_many="rate",
        one_of_many_required=False,
    )

    route: fhirtypes.CodeableConceptType = Field(
        None,
        alias="route",
        title="Path of substance into body",
        description=(
            "A code specifying the route or physiological path of administration of"
            " a therapeutic agent into or onto the patient.  For example, topical, "
            "intravenous, etc."
        ),
    )

    site: fhirtypes.CodeableConceptType = Field(
        None,
        alias="site",
        title="Body site administered to",
        description=(
            "A coded specification of the anatomic site where the medication first "
            'entered the body.  For example, "left arm".'
        ),
    )

    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Free text dosage instructions e.g. SIG",
        description=(
            "Free text dosage can be used for cases where the dosage administered "
            "is too complex to code. When coded dosage is present, the free text "
            "dosage may still be present for display to humans.  The dosage "
            "instructions should reflect the dosage of the medication that was "
            "administered."
        ),
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
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
        one_of_many_fields = {"rate": ["rateQuantity", "rateRatio"]}
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


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who administered substance.
    The individual who was responsible for giving the medication to the
    patient.
    """

    resource_type = Field("MedicationAdministrationPerformer", const=True)

    actor: fhirtypes.ReferenceType = Field(
        ...,
        alias="actor",
        title="Individual who was performing",
        description="The device, practitioner, etc. who performed the action.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Patient", "RelatedPerson", "Device"],
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title="Organization organization was acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )
