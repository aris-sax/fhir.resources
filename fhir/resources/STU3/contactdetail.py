# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ContactDetail
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import element, fhirtypes


class ContactDetail(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Contact information.
    Specifies contact information for a person or organization.
    """

    resource_type = Field("ContactDetail", const=True)

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of an individual to contact",
        description="The name of an individual to contact.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details for individual or organization",
        description=(
            "The contact details for the individual (if a name was provided) or the"
            " organization."
        ),
    )
