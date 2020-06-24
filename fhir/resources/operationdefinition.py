# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class OperationDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an operation or a named query.
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """

    resource_type = Field("OperationDefinition", const=True)

    affectsState: bool = Field(
        None,
        alias="affectsState",
        title="Whether content is changed by the operation",
        description=(
            "Whether the operation affects state. Side effects such as producing "
            "audit trail entries do not count as 'affecting  state'."
        ),
    )
    affectsState__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_affectsState", title="Extension field for ``affectsState``."
    )

    base: fhirtypes.Canonical = Field(
        None,
        alias="base",
        title="Marks this as a profile of the base",
        description=(
            "Indicates that this operation definition is a constraining profile on "
            "the base."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationDefinition"],
    )
    base__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_base", title="Extension field for ``base``."
    )

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Name used to invoke the operation",
        description="The name used to invoke the operation.",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    comment: fhirtypes.Markdown = Field(
        None,
        alias="comment",
        title="Additional information about use",
        description="Additional information about how to use this operation or named query.",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
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

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the operation definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the operation definition "
            "changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the operation definition",
        description=(
            "A free text natural language description of the operation definition "
            "from a consumer's perspective."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this operation definition is authored"
            " for testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    inputProfile: fhirtypes.Canonical = Field(
        None,
        alias="inputProfile",
        title="Validation information for in parameters",
        description=(
            "Additional validation information for the in parameters - a single "
            "profile that covers all the parameters. The profile is a constraint on"
            " the parameters resource as a whole."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    inputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inputProfile", title="Extension field for ``inputProfile``."
    )

    instance: bool = Field(
        ...,
        alias="instance",
        title="Invoke on an instance?",
        description=(
            "Indicates whether this operation can be invoked on a particular "
            "instance of one of the given types."
        ),
    )
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instance", title="Extension field for ``instance``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for operation definition (if applicable)",
        description=(
            "A legal or geographic region in which the operation definition is "
            "intended to be used."
        ),
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="operation | query",
        description="Whether this is an operation or a named query.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["operation", "query"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this operation definition (computer friendly)",
        description=(
            "A natural language name identifying the operation definition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    outputProfile: fhirtypes.Canonical = Field(
        None,
        alias="outputProfile",
        title="Validation information for out parameters",
        description=(
            "Additional validation information for the out parameters - a single "
            "profile that covers all the parameters. The profile is a constraint on"
            " the parameters resource."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    outputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outputProfile", title="Extension field for ``outputProfile``."
    )

    overload: ListType[fhirtypes.OperationDefinitionOverloadType] = Field(
        None,
        alias="overload",
        title="Define overloaded variants for when  generating code",
        description=(
            "Defines an appropriate combination of parameters to use when invoking "
            "this operation, to help code generators when generating overloaded "
            "parameter sets for this operation."
        ),
    )

    parameter: ListType[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="parameter",
        title="Parameters for the operation/query",
        description="The parameters for the operation/query.",
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "operation definition."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this operation definition is defined",
        description=(
            "Explanation of why this operation definition is needed and why it has "
            "been designed as it has."
        ),
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resource: ListType[fhirtypes.Code] = Field(
        None,
        alias="resource",
        title="Types this operation applies to",
        description="The types on which this operation can be executed.",
    )
    resource__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_resource", title="Extension field for ``resource``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this operation definition. Enables tracking the life-"
            "cycle of the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    system: bool = Field(
        ...,
        alias="system",
        title="Invoke at the system level?",
        description=(
            "Indicates whether this operation or named query can be invoked at the "
            "system level (e.g. without needing to choose a resource type for the "
            "context)."
        ),
    )
    system__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_system", title="Extension field for ``system``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this operation definition (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the operation " "definition."
        ),
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: bool = Field(
        ...,
        alias="type",
        title="Invoke at the type level?",
        description=(
            "Indicates whether this operation or named query can be invoked at the "
            "resource type level for any given resource type level (e.g. without "
            "needing to choose a specific resource id for the context)."
        ),
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this operation definition, represented as a "
            "URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this operation definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this operation definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the operation definition is stored on "
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
            "indexing and searching for appropriate operation definition instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the operation definition",
        description=(
            "The identifier that is used to identify this version of the operation "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the operation "
            "definition author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class OperationDefinitionOverload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Define overloaded variants for when  generating code.
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """

    resource_type = Field("OperationDefinitionOverload", const=True)

    comment: fhirtypes.String = Field(
        None, alias="comment", title="Comments to go on overload", description=None,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    parameterName: ListType[fhirtypes.String] = Field(
        None,
        alias="parameterName",
        title="Name of parameter to include in overload",
        description=None,
    )
    parameterName__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_parameterName", title="Extension field for ``parameterName``."
    )


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Parameters for the operation/query.
    The parameters for the operation/query.
    """

    resource_type = Field("OperationDefinitionParameter", const=True)

    binding: fhirtypes.OperationDefinitionParameterBindingType = Field(
        None,
        alias="binding",
        title="ValueSet details if this is coded",
        description=(
            "Binds to a value set if this parameter is coded (code, Coding, "
            "CodeableConcept)."
        ),
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Description of meaning/use",
        description="Describes the meaning or use of this parameter.",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    max: fhirtypes.String = Field(
        ...,
        alias="max",
        title="Maximum Cardinality (a number or *)",
        description=(
            "The maximum number of times this element is permitted to appear in the"
            " request or response."
        ),
    )
    max__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_max", title="Extension field for ``max``."
    )

    min: fhirtypes.Integer = Field(
        ...,
        alias="min",
        title="Minimum Cardinality",
        description=(
            "The minimum number of times this parameter SHALL appear in the request"
            " or response."
        ),
    )
    min__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_min", title="Extension field for ``min``."
    )

    name: fhirtypes.Code = Field(
        ...,
        alias="name",
        title="Name in Parameters.parameter.name or in URL",
        description="The name of used to identify the parameter.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    part: ListType[fhirtypes.OperationDefinitionParameterType] = Field(
        None,
        alias="part",
        title="Parts of a nested Parameter",
        description="The parts of a nested Parameter.",
    )

    referencedFrom: ListType[
        fhirtypes.OperationDefinitionParameterReferencedFromType
    ] = Field(
        None,
        alias="referencedFrom",
        title="References to this parameter",
        description=(
            "Identifies other resource parameters within the operation invocation "
            "that are expected to resolve to this resource."
        ),
    )

    searchType: fhirtypes.Code = Field(
        None,
        alias="searchType",
        title=(
            "number | date | string | token | reference | composite | quantity | "
            "uri | special"
        ),
        description=(
            "How the parameter is understood as a search parameter. This is only "
            "used if the parameter type is 'string'."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
            "special",
        ],
    )
    searchType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_searchType", title="Extension field for ``searchType``."
    )

    targetProfile: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="targetProfile",
        title="If type is Reference | canonical, allowed targets",
        description=(
            'Used when the type is "Reference" or "canonical", and identifies a '
            "profile structure or implementation Guide that applies to the target "
            "of the reference this parameter refers to. If any profiles are "
            "specified, then the content must conform to at least one of them. The "
            "URL can be a local reference - to a contained StructureDefinition, or "
            "a reference to another StructureDefinition or Implementation Guide by "
            "a canonical URL. When an implementation guide is specified, the target"
            " resource SHALL conform to at least one profile defined in the "
            "implementation guide."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )
    targetProfile__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_targetProfile", title="Extension field for ``targetProfile``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="What type this parameter has",
        description="The type for this parameter.",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    use: fhirtypes.Code = Field(
        ...,
        alias="use",
        title="in | out",
        description="Whether this is an input or an output parameter.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["in", "out"],
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    ValueSet details if this is coded.
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """

    resource_type = Field("OperationDefinitionParameterBinding", const=True)

    strength: fhirtypes.Code = Field(
        ...,
        alias="strength",
        title="required | extensible | preferred | example",
        description=(
            "Indicates the degree of conformance expectations associated with this "
            "binding - that is, the degree to which the provided value set must be "
            "adhered to in the instances."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["required", "extensible", "preferred", "example"],
    )
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_strength", title="Extension field for ``strength``."
    )

    valueSet: fhirtypes.Canonical = Field(
        ...,
        alias="valueSet",
        title="Source of value set",
        description=(
            "Points to the value set or external definition (e.g. implicit value "
            "set) that identifies the set of codes to be used."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    References to this parameter.
    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """

    resource_type = Field("OperationDefinitionParameterReferencedFrom", const=True)

    source: fhirtypes.String = Field(
        ...,
        alias="source",
        title="Referencing parameter",
        description=(
            "The name of the parameter or dot-separated path of parameter names "
            "pointing to the resource parameter that is expected to contain a "
            "reference to this resource."
        ),
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    sourceId: fhirtypes.String = Field(
        None,
        alias="sourceId",
        title="Element id of reference",
        description=(
            "The id of the element in the referencing resource that is expected to "
            "resolve to this resource."
        ),
    )
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceId", title="Extension field for ``sourceId``."
    )
