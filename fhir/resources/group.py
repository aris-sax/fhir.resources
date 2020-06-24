# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Group(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Group of multiple entities.
    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """

    resource_type = Field("Group", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this group's record is in active use",
        description=(
            "Indicates whether the record for the group is available for use or is "
            "merely being retained for historical purposes."
        ),
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    actual: bool = Field(
        ...,
        alias="actual",
        title="Descriptive or actual",
        description=(
            "If true, indicates that the resource refers to a specific group of "
            "real individuals.  If false, the group defines a set of intended "
            "individuals."
        ),
    )
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actual", title="Extension field for ``actual``."
    )

    characteristic: ListType[fhirtypes.GroupCharacteristicType] = Field(
        None,
        alias="characteristic",
        title="Include / Exclude group members by Trait",
        description=(
            "Identifies traits whose presence r absence is shared by members of the"
            " group."
        ),
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Kind of Group members",
        description=(
            'Provides a specific type of resource the group includes; e.g. "cow", '
            '"syringe", etc.'
        ),
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique id",
        description="A unique business identifier for this group.",
    )

    managingEntity: fhirtypes.ReferenceType = Field(
        None,
        alias="managingEntity",
        title="Entity that is the custodian of the Group's definition",
        description=(
            "Entity responsible for defining and maintaining Group characteristics "
            "and/or registered members."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Organization",
            "RelatedPerson",
            "Practitioner",
            "PractitionerRole",
        ],
    )

    member: ListType[fhirtypes.GroupMemberType] = Field(
        None,
        alias="member",
        title="Who or what is in group",
        description="Identifies the resource instances that are members of the group.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Label for Group",
        description=(
            "A label assigned to the group for human identification and "
            "communication."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    quantity: fhirtypes.UnsignedInt = Field(
        None,
        alias="quantity",
        title="Number of members",
        description=(
            "A count of the number of resource instances that are part of the " "group."
        ),
    )
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_quantity", title="Extension field for ``quantity``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="person | animal | practitioner | device | medication | substance",
        description=(
            "Identifies the broad classification of the kind of resources the group"
            " includes."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "person",
            "animal",
            "practitioner",
            "device",
            "medication",
            "substance",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class GroupCharacteristic(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Include / Exclude group members by Trait.
    Identifies traits whose presence r absence is shared by members of the
    group.
    """

    resource_type = Field("GroupCharacteristic", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Kind of characteristic",
        description="A code that identifies the kind of trait being asserted.",
    )

    exclude: bool = Field(
        ...,
        alias="exclude",
        title="Group includes or excludes",
        description=(
            "If true, indicates the characteristic is one that is NOT held by "
            "members of the group."
        ),
    )
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_exclude", title="Extension field for ``exclude``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period over which characteristic is tested",
        description=(
            "The period over which the characteristic is tested; e.g. the patient "
            "had an operation during the month of June."
        ),
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="Value held by characteristic",
        description=(
            "The value of the trait that holds (or does not hold - see 'exclude') "
            "for members of the group."
        ),
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
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
            "value": [
                "valueBoolean",
                "valueCodeableConcept",
                "valueQuantity",
                "valueRange",
                "valueReference",
            ]
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


class GroupMember(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who or what is in group.
    Identifies the resource instances that are members of the group.
    """

    resource_type = Field("GroupMember", const=True)

    entity: fhirtypes.ReferenceType = Field(
        ...,
        alias="entity",
        title="Reference to the group member",
        description=(
            "A reference to the entity that is a member of the group. Must be "
            "consistent with Group.type. If the entity is another group, then the "
            "type must be the same."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "Device",
            "Medication",
            "Substance",
            "Group",
        ],
    )

    inactive: bool = Field(
        None,
        alias="inactive",
        title="If member is no longer in group",
        description=(
            "A flag to indicate that the member is no longer in the group, but "
            "previously may have been a member."
        ),
    )
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inactive", title="Extension field for ``inactive``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period member belonged to the group",
        description="The period that the member was in the group, if known.",
    )
