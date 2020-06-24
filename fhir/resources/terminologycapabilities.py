# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class TerminologyCapabilities(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """

    resource_type = Field("TerminologyCapabilities", const=True)

    closure: fhirtypes.TerminologyCapabilitiesClosureType = Field(
        None,
        alias="closure",
        title=(
            "Information about the [ConceptMap/$closure](conceptmap-operation-"
            "closure.html) operation"
        ),
        description="Whether the $closure operation is supported.",
    )

    codeSearch: fhirtypes.Code = Field(
        None,
        alias="codeSearch",
        title="explicit | all",
        description=(
            "The degree to which the server supports the code search parameter on "
            "ValueSet, if it is supported."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["explicit", "all"],
    )
    codeSearch__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_codeSearch", title="Extension field for ``codeSearch``."
    )

    codeSystem: ListType[fhirtypes.TerminologyCapabilitiesCodeSystemType] = Field(
        None,
        alias="codeSystem",
        title="A code system supported by the server",
        description=(
            "Identifies a code system that is supported by the server. If there is "
            "a no code system URL, then this declares the general assumptions a "
            "client can make about support for any CodeSystem resource."
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
            "A copyright statement relating to the terminology capabilities and/or "
            "its contents. Copyright statements are generally legal restrictions on"
            " the use and publishing of the terminology capabilities."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the terminology capabilities was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the terminology capabilities "
            "changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the terminology capabilities",
        description=(
            "A free text natural language description of the terminology "
            "capabilities from a consumer's perspective. Typically, this is used "
            "when the capability statement describes a desired rather than an "
            "actual solution, for example as a formal expression of requirements as"
            " part of an RFP."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    expansion: fhirtypes.TerminologyCapabilitiesExpansionType = Field(
        None,
        alias="expansion",
        title=(
            "Information about the [ValueSet/$expand](valueset-operation-"
            "expand.html) operation"
        ),
        description=None,
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this terminology capabilities is "
            "authored for testing purposes (or education/evaluation/marketing) and "
            "is not intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    implementation: fhirtypes.TerminologyCapabilitiesImplementationType = Field(
        None,
        alias="implementation",
        title="If this describes a specific instance",
        description=(
            "Identifies a specific implementation instance that is described by the"
            " terminology capability statement - i.e. a particular installation, "
            "rather than the capabilities of a software program."
        ),
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for terminology capabilities (if applicable)",
        description=(
            "A legal or geographic region in which the terminology capabilities is "
            "intended to be used."
        ),
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="instance | capability | requirements",
        description=(
            "The way that this statement is intended to be used, to describe an "
            "actual running instance of software, a particular product (kind, not "
            "instance of software) or a class of implementation (e.g. a desired "
            "purchase)."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "capability", "requirements"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    lockedDate: bool = Field(
        None,
        alias="lockedDate",
        title="Whether lockedDate is supported",
        description="Whether the server supports lockedDate.",
    )
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lockedDate", title="Extension field for ``lockedDate``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this terminology capabilities (computer friendly)",
        description=(
            "A natural language name identifying the terminology capabilities. This"
            " name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "terminology capabilities."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this terminology capabilities is defined",
        description=(
            "Explanation of why this terminology capabilities is needed and why it "
            "has been designed as it has."
        ),
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    software: fhirtypes.TerminologyCapabilitiesSoftwareType = Field(
        None,
        alias="software",
        title="Software that is covered by this terminology capability statement",
        description=(
            "Software that is covered by this terminology capability statement.  It"
            " is used when the statement describes the capabilities of a particular"
            " software version, independent of an installation."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this terminology capabilities. Enables tracking the "
            "life-cycle of the content."
        ),
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
        title="Name for this terminology capabilities (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the terminology "
            "capabilities."
        ),
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    translation: fhirtypes.TerminologyCapabilitiesTranslationType = Field(
        None,
        alias="translation",
        title=(
            "Information about the [ConceptMap/$translate](conceptmap-operation-"
            "translate.html) operation"
        ),
        description=None,
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this terminology capabilities, represented as"
            " a URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this terminology capabilities"
            " when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this terminology capabilities is (or will "
            "be) published. This URL can be the target of a canonical reference. It"
            " SHALL remain the same when the terminology capabilities is stored on "
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
            "indexing and searching for appropriate terminology capabilities "
            "instances."
        ),
    )

    validateCode: fhirtypes.TerminologyCapabilitiesValidateCodeType = Field(
        None,
        alias="validateCode",
        title=(
            "Information about the [ValueSet/$validate-code](valueset-operation-"
            "validate-code.html) operation"
        ),
        description=None,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the terminology capabilities",
        description=(
            "The identifier that is used to identify this version of the "
            "terminology capabilities when it is referenced in a specification, "
            "model, design or instance. This is an arbitrary value managed by the "
            "terminology capabilities author and is not expected to be globally "
            "unique. For example, it might be a timestamp (e.g. yyyymmdd) if a "
            "managed version is not available. There is also no expectation that "
            "versions can be placed in a lexicographical sequence."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.
    Whether the $closure operation is supported.
    """

    resource_type = Field("TerminologyCapabilitiesClosure", const=True)

    translation: bool = Field(
        None,
        alias="translation",
        title="If cross-system closure is supported",
        description=None,
    )
    translation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_translation", title="Extension field for ``translation``."
    )


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A code system supported by the server.
    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystem", const=True)

    subsumption: bool = Field(
        None,
        alias="subsumption",
        title="Whether subsumption is supported",
        description="True if subsumption is supported for this version of the code system.",
    )
    subsumption__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subsumption", title="Extension field for ``subsumption``."
    )

    uri: fhirtypes.Canonical = Field(
        None,
        alias="uri",
        title="URI for the Code System",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CodeSystem"],
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )

    version: ListType[fhirtypes.TerminologyCapabilitiesCodeSystemVersionType] = Field(
        None,
        alias="version",
        title="Version of Code System supported",
        description=(
            "For the code system, a list of versions that are supported by the "
            "server."
        ),
    )


class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Version of Code System supported.
    For the code system, a list of versions that are supported by the server.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystemVersion", const=True)

    code: fhirtypes.String = Field(
        None,
        alias="code",
        title="Version identifier for this version",
        description=(
            "For version-less code systems, there should be a single version with "
            "no identifier."
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    compositional: bool = Field(
        None,
        alias="compositional",
        title="If compositional grammar is supported",
        description="If the compositional grammar defined by the code system is supported.",
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_compositional", title="Extension field for ``compositional``."
    )

    filter: ListType[
        fhirtypes.TerminologyCapabilitiesCodeSystemVersionFilterType
    ] = Field(
        None, alias="filter", title="Filter Properties supported", description=None,
    )

    isDefault: bool = Field(
        None,
        alias="isDefault",
        title="If this is the default version for this code system",
        description=None,
    )
    isDefault__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDefault", title="Extension field for ``isDefault``."
    )

    language: ListType[fhirtypes.Code] = Field(
        None, alias="language", title="Language Displays supported", description=None,
    )
    language__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    property: ListType[fhirtypes.Code] = Field(
        None,
        alias="property",
        title="Properties supported for $lookup",
        description=None,
    )
    property__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_property", title="Extension field for ``property``."
    )


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter Properties supported.
    """

    resource_type = Field("TerminologyCapabilitiesCodeSystemVersionFilter", const=True)

    code: fhirtypes.Code = Field(
        ..., alias="code", title="Code of the property supported", description=None,
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    op: ListType[fhirtypes.Code] = Field(
        ...,
        alias="op",
        title="Operations supported for the property",
        description=None,
    )
    op__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_op", title="Extension field for ``op``."
    )


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """

    resource_type = Field("TerminologyCapabilitiesExpansion", const=True)

    hierarchical: bool = Field(
        None,
        alias="hierarchical",
        title="Whether the server can return nested value sets",
        description=None,
    )
    hierarchical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_hierarchical", title="Extension field for ``hierarchical``."
    )

    incomplete: bool = Field(
        None,
        alias="incomplete",
        title="Allow request for incomplete expansions?",
        description="Allow request for incomplete expansions?",
    )
    incomplete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_incomplete", title="Extension field for ``incomplete``."
    )

    paging: bool = Field(
        None,
        alias="paging",
        title="Whether the server supports paging on expansion",
        description=None,
    )
    paging__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_paging", title="Extension field for ``paging``."
    )

    parameter: ListType[
        fhirtypes.TerminologyCapabilitiesExpansionParameterType
    ] = Field(
        None,
        alias="parameter",
        title="Supported expansion parameter",
        description=None,
    )

    textFilter: fhirtypes.Markdown = Field(
        None,
        alias="textFilter",
        title="Documentation about text searching works",
        description=None,
    )
    textFilter__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_textFilter", title="Extension field for ``textFilter``."
    )


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Supported expansion parameter.
    """

    resource_type = Field("TerminologyCapabilitiesExpansionParameter", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Description of support for parameter",
        description=None,
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.Code = Field(
        ..., alias="name", title="Expansion Parameter name", description=None,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """

    resource_type = Field("TerminologyCapabilitiesImplementation", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Describes this specific instance",
        description=(
            "Information about the specific installation that this terminology "
            "capability statement relates to."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Url = Field(
        None,
        alias="url",
        title="Base URL for the implementation",
        description="An absolute base URL for the implementation.",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this terminology capability statement.
    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("TerminologyCapabilitiesSoftware", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="A name the software is known by",
        description="Name the software is known by.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version covered by this statement",
        description="The version identifier for the software covered by this statement.",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """

    resource_type = Field("TerminologyCapabilitiesTranslation", const=True)

    needsMap: bool = Field(
        ...,
        alias="needsMap",
        title="Whether the client must identify the map",
        description=None,
    )
    needsMap__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_needsMap", title="Extension field for ``needsMap``."
    )


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """

    resource_type = Field("TerminologyCapabilitiesValidateCode", const=True)

    translations: bool = Field(
        ...,
        alias="translations",
        title="Whether translations are validated",
        description=None,
    )
    translations__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_translations", title="Extension field for ``translations``."
    )
