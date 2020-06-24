# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SupplyDelivery(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Delivery of bulk Supplies.
    Record of delivery of what is supplied.
    """

    resource_type = Field("SupplyDelivery", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Fulfills plan, proposal or order",
        description=(
            "A plan, proposal or order that is fulfilled in whole or in part by "
            "this event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SupplyRequest"],
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title="Where the Supply was sent",
        description=(
            "Identification of the facility/location where the Supply was shipped "
            "to, as part of the dispense event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifier for the supply delivery event that is used to identify it "
            "across multiple disparate systems."
        ),
    )

    occurrenceDateTime: fhirtypes.DateTime = Field(
        None,
        alias="occurrenceDateTime",
        title="When event occurred",
        description="The date or time(s) the activity occurred.",
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
        title="When event occurred",
        description="The date or time(s) the activity occurred.",
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    occurrenceTiming: fhirtypes.TimingType = Field(
        None,
        alias="occurrenceTiming",
        title="When event occurred",
        description="The date or time(s) the activity occurred.",
        # Choice of Data Types. i.e occurrence[x]
        one_of_many="occurrence",
        one_of_many_required=False,
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of referenced event",
        description="A larger event of which this particular event is a component or step.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["SupplyDelivery", "Contract"],
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Patient for whom the item is supplied",
        description=(
            "A link to a resource representing the person whom the delivered item "
            "is for."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    receiver: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="receiver",
        title="Who collected the Supply",
        description="Identifies the person who picked up the Supply.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="in-progress | completed | abandoned | entered-in-error",
        description="A code specifying the state of the dispense event.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in-progress", "completed", "abandoned", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    suppliedItem: fhirtypes.SupplyDeliverySuppliedItemType = Field(
        None,
        alias="suppliedItem",
        title="The item that is delivered or supplied",
        description="The item that is being delivered or has been supplied.",
    )

    supplier: fhirtypes.ReferenceType = Field(
        None,
        alias="supplier",
        title="Dispenser",
        description=(
            "The individual responsible for dispensing the medication, supplier or "
            "device."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Category of dispense event",
        description=(
            "Indicates the type of dispensing event that is performed. Examples "
            "include: Trial Fill, Completion of Trial, Partial Fill, Emergency "
            "Fill, Samples, etc."
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
            "occurrence": ["occurrenceDateTime", "occurrencePeriod", "occurrenceTiming"]
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


class SupplyDeliverySuppliedItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The item that is delivered or supplied.
    The item that is being delivered or has been supplied.
    """

    resource_type = Field("SupplyDeliverySuppliedItem", const=True)

    itemCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="itemCodeableConcept",
        title="Medication, Substance, or Device supplied",
        description=(
            "Identifies the medication, substance or device being dispensed. This "
            "is either a link to a resource representing the details of the item or"
            " a code that identifies the item from a known list."
        ),
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=False,
    )

    itemReference: fhirtypes.ReferenceType = Field(
        None,
        alias="itemReference",
        title="Medication, Substance, or Device supplied",
        description=(
            "Identifies the medication, substance or device being dispensed. This "
            "is either a link to a resource representing the details of the item or"
            " a code that identifies the item from a known list."
        ),
        # Choice of Data Types. i.e item[x]
        one_of_many="item",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication", "Substance", "Device"],
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Amount dispensed",
        description=(
            "The amount of supply that has been dispensed. Includes unit of " "measure."
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
        one_of_many_fields = {"item": ["itemCodeableConcept", "itemReference"]}
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
