# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Identifier
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Identifier(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An identifier intended for computation.
    A technical identifier - identifies some entity uniquely and unambiguously.
    """

    resource_type = Field("Identifier", const=True)

    assigner: fhirtypes.ReferenceType = Field(
        None,
        alias="assigner",
        title="Organization that issued id (may be just text)",
        description="Organization that issued/manages the identifier.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Time period when id is/was valid for use",
        description="Time period during which identifier is/was valid for use.",
    )

    system: fhirtypes.Uri = Field(
        None,
        alias="system",
        title="The namespace for the identifier value",
        description=(
            "Establishes the namespace for the value - that is, a URL that "
            "describes a set values that are unique."
        ),
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Description of identifier",
        description=(
            "A coded type for the identifier that can be used to determine which "
            "identifier to use for a specific purpose."
        ),
    )

    use: fhirtypes.Code = Field(
        None,
        alias="use",
        title="usual | official | temp | secondary (If known)",
        description="The purpose of this identifier.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["usual", "official", "temp", "secondary (If known)"],
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    value: fhirtypes.String = Field(
        None,
        alias="value",
        title="The value that is unique",
        description=(
            "The portion of the identifier typically relevant to the user and which"
            " is unique within the context of the system."
        ),
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
