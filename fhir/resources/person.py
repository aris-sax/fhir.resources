# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Person(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A generic person record.
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type = Field("Person", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="This person's record is in active use",
        description="Whether this person's record is in active use.",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None,
        alias="address",
        title="One or more addresses for the person",
        description=None,
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="The date on which the person was born",
        description="The birth date for the person.",
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description="Administrative Gender.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="A human identifier for this person",
        description="Identifier for a person within a particular scope.",
    )

    link: ListType[fhirtypes.PersonLinkType] = Field(
        None,
        alias="link",
        title="Link to a resource that concerns the same actual person",
        description=None,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="The organization that is the custodian of the person record",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None, alias="name", title="A name associated with the person", description=None,
    )

    photo: fhirtypes.AttachmentType = Field(
        None,
        alias="photo",
        title="Image of the person",
        description=(
            "An image that can be displayed as a thumbnail of the person to enhance"
            " the identification of the individual."
        ),
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the person",
        description=(
            "A contact detail for the person, e.g. a telephone number or an email "
            "address."
        ),
    )


class PersonLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to a resource that concerns the same actual person.
    """

    resource_type = Field("PersonLink", const=True)

    assurance: fhirtypes.Code = Field(
        None,
        alias="assurance",
        title="level1 | level2 | level3 | level4",
        description=(
            "Level of assurance that this link is associated with the target "
            "resource."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["level1", "level2", "level3", "level4"],
    )
    assurance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_assurance", title="Extension field for ``assurance``."
    )

    target: fhirtypes.ReferenceType = Field(
        ...,
        alias="target",
        title="The resource to which this actual person is associated",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Practitioner", "RelatedPerson", "Person"],
    )
