# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class ChargeItemDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.
    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """

    resource_type = Field("ChargeItemDefinition", const=True)

    applicability: ListType[fhirtypes.ChargeItemDefinitionApplicabilityType] = Field(
        None,
        alias="applicability",
        title="Whether or not the billing code is applicable",
        description="Expressions that describe applicability criteria for the billing code.",
    )

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the charge item definition was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Billing codes or product types this definition applies to",
        description=(
            "The defined billing details in this resource pertain to the given "
            "billing code."
        ),
    )

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the charge item definition and/or "
            "its contents. Copyright statements are generally legal restrictions on"
            " the use and publishing of the charge item definition."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the charge item definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the charge item definition "
            "changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    derivedFromUri: ListType[fhirtypes.Uri] = Field(
        None,
        alias="derivedFromUri",
        title="Underlying externally-defined charge item definition",
        description=(
            "The URL pointing to an externally-defined charge item definition that "
            "is adhered to in whole or in part by this definition."
        ),
    )
    derivedFromUri__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_derivedFromUri", title="Extension field for ``derivedFromUri``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the charge item definition",
        description=(
            "A free text natural language description of the charge item definition"
            " from a consumer's perspective."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the charge item definition is expected to be used",
        description=(
            "The period during which the charge item definition content was or is "
            "planned to be in active use."
        ),
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this charge item definition is "
            "authored for testing purposes (or education/evaluation/marketing) and "
            "is not intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the charge item definition",
        description=(
            "A formal identifier that is used to identify this charge item "
            "definition when it is represented in other formats, or referenced in a"
            " specification, model, design or an instance."
        ),
    )

    instance: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="instance",
        title="Instances this definition applies to",
        description=(
            "The defined billing details in this resource pertain to the given "
            "product instance(s)."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Medication", "Substance", "Device"],
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for charge item definition (if applicable)",
        description=(
            "A legal or geographic region in which the charge item definition is "
            "intended to be used."
        ),
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the charge item definition was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    partOf: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="partOf",
        title=(
            "A larger definition of which this particular definition is a component"
            " or step"
        ),
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItemDefinition"],
    )
    partOf__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_partOf", title="Extension field for ``partOf``."
    )

    propertyGroup: ListType[fhirtypes.ChargeItemDefinitionPropertyGroupType] = Field(
        None,
        alias="propertyGroup",
        title="Group of properties which are applicable under the same conditions",
        description=(
            "Group of properties which are applicable under the same conditions. If"
            " no applicability rules are established for the group, then all "
            "properties always apply."
        ),
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the charge "
            "item definition."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    replaces: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="replaces",
        title=(
            "Completed or terminated request(s) whose function is taken by this new"
            " request"
        ),
        description=(
            "As new versions of a protocol or guideline are defined, allows "
            "identification of what versions are replaced by a new instance."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ChargeItemDefinition"],
    )
    replaces__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_replaces", title="Extension field for ``replaces``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description="The current state of the ChargeItemDefinition.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this charge item definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the charge item "
            "definition."
        ),
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title=(
            "Canonical identifier for this charge item definition, represented as a"
            " URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this charge item definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this charge item definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the charge item definition is stored on "
            "different servers."
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate charge item definition "
            "instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the charge item definition",
        description=(
            "The identifier that is used to identify this version of the charge "
            "item definition when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the charge "
            "item definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence. To provide a version consistent "
            "with the Decision Support Service specification, use the format "
            "Major.Minor.Revision (e.g. 1.0.0). For more information on versioning "
            "knowledge assets, refer to the Decision Support Service specification."
            " Note that a version is required for non-experimental active assets."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the billing code is applicable.
    Expressions that describe applicability criteria for the billing code.
    """

    resource_type = Field("ChargeItemDefinitionApplicability", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Natural language description of the condition",
        description=(
            "A brief, natural language description of the condition that "
            "effectively communicates the intended semantics."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expression: fhirtypes.String = Field(
        None,
        alias="expression",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether the "
            "condition is satisfied. When using FHIRPath expressions, the %context "
            "environment variable must be replaced at runtime with the ChargeItem "
            "resource to which this definition is applied."
        ),
    )
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expression", title="Extension field for ``expression``."
    )

    language: fhirtypes.String = Field(
        None,
        alias="language",
        title="Language of the expression",
        description=(
            'The media type of the language for the expression, e.g. "text/cql" for'
            ' Clinical Query Language expressions or "text/fhirpath" for FHIRPath '
            "expressions."
        ),
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )


class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Group of properties which are applicable under the same conditions.
    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """

    resource_type = Field("ChargeItemDefinitionPropertyGroup", const=True)

    applicability: ListType[fhirtypes.ChargeItemDefinitionApplicabilityType] = Field(
        None,
        alias="applicability",
        title="Conditions under which the priceComponent is applicable",
        description=(
            "Expressions that describe applicability criteria for the "
            "priceComponent."
        ),
    )

    priceComponent: ListType[
        fhirtypes.ChargeItemDefinitionPropertyGroupPriceComponentType
    ] = Field(
        None,
        alias="priceComponent",
        title="Components of total line item price",
        description=(
            "The price for a ChargeItem may be calculated as a base price with "
            "surcharges/deductions that apply in certain conditions. A "
            "ChargeItemDefinition resource that defines the prices, factors and "
            "conditions that apply to a billing code is currently under "
            "development. The priceComponent element can be used to offer "
            "transparency to the recipient of the Invoice of how the prices have "
            "been calculated."
        ),
    )


class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Components of total line item price.
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """

    resource_type = Field("ChargeItemDefinitionPropertyGroupPriceComponent", const=True)

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Monetary amount associated with this component",
        description="The amount calculated for this component.",
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="Code identifying the specific component",
        description=(
            "A code that identifies the component. Codes may be used to "
            "differentiate between kinds of taxes, surcharges, discounts etc."
        ),
    )

    factor: fhirtypes.Decimal = Field(
        None,
        alias="factor",
        title="Factor used for calculating this component",
        description=(
            "The factor that has been applied on the base price for calculating "
            "this component."
        ),
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="base | surcharge | deduction | discount | tax | informational",
        description="This code identifies the type of the component.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "base",
            "surcharge",
            "deduction",
            "discount",
            "tax",
            "informational",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
