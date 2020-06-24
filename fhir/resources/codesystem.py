# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CodeSystem
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class CodeSystem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Declares the existence of and describes a code system or code system
    supplement.
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """

    resource_type = Field("CodeSystem", const=True)

    caseSensitive: bool = Field(
        None,
        alias="caseSensitive",
        title="If code comparison is case sensitive",
        description=(
            "If code comparison is case sensitive when codes within this system are"
            " compared to each other."
        ),
    )
    caseSensitive__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_caseSensitive", title="Extension field for ``caseSensitive``."
    )

    compositional: bool = Field(
        None,
        alias="compositional",
        title="If code system defines a compositional grammar",
        description="The code system defines a compositional (post-coordination) grammar.",
    )
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_compositional", title="Extension field for ``compositional``."
    )

    concept: ListType[fhirtypes.CodeSystemConceptType] = Field(
        None,
        alias="concept",
        title="Concepts in the code system",
        description=(
            "Concepts that are in the code system. The concept definitions are "
            "inherently hierarchical, but the definitions must be consulted to "
            "determine what the meanings of the hierarchical relationships are."
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

    content: fhirtypes.Code = Field(
        ...,
        alias="content",
        title="not-present | example | fragment | complete | supplement",
        description=(
            "The extent of the content of the code system (the concepts and codes "
            "it defines) are represented in this resource instance."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["not-present", "example", "fragment", "complete", "supplement"],
    )
    content__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_content", title="Extension field for ``content``."
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the code system and/or its contents."
            " Copyright statements are generally legal restrictions on the use and "
            "publishing of the code system."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    count: fhirtypes.UnsignedInt = Field(
        None,
        alias="count",
        title="Total concepts in the code system",
        description=(
            "The total number of concepts defined by the code system. Where the "
            "code system has a compositional grammar, the basis of this count is "
            "defined by the system steward."
        ),
    )
    count__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_count", title="Extension field for ``count``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the code system was published. "
            "The date must change when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the code system changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the code system",
        description=(
            "A free text natural language description of the code system from a "
            "consumer's perspective."
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
            "A Boolean value to indicate that this code system is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    filter: ListType[fhirtypes.CodeSystemFilterType] = Field(
        None,
        alias="filter",
        title="Filter that can be used in a value set",
        description=(
            "A filter that can be used in a value set compose statement when "
            "selecting concepts using a filter."
        ),
    )

    hierarchyMeaning: fhirtypes.Code = Field(
        None,
        alias="hierarchyMeaning",
        title="grouped-by | is-a | part-of | classified-with",
        description=(
            "The meaning of the hierarchy of concepts as represented in this "
            "resource."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["grouped-by", "is-a", "part-of", "classified-with"],
    )
    hierarchyMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_hierarchyMeaning",
        title="Extension field for ``hierarchyMeaning``.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the code system (business identifier)",
        description=(
            "A formal identifier that is used to identify this code system when it "
            "is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for code system (if applicable)",
        description=(
            "A legal or geographic region in which the code system is intended to "
            "be used."
        ),
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this code system (computer friendly)",
        description=(
            "A natural language name identifying the code system. This name should "
            "be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    property: ListType[fhirtypes.CodeSystemPropertyType] = Field(
        None,
        alias="property",
        title="Additional information supplied about each concept",
        description=(
            "A property defines an additional slot through which additional "
            "information can be provided about a concept."
        ),
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the code "
            "system."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this code system is defined",
        description=(
            "Explanation of why this code system is needed and why it has been "
            "designed as it has."
        ),
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The date (and optionally time) when the code system resource was "
            "created or revised."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    supplements: fhirtypes.Canonical = Field(
        None,
        alias="supplements",
        title="Canonical URL of Code System this adds designations and properties to",
        description=(
            "The canonical URL of the code system that this code system supplement "
            "is adding designations and properties to."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CodeSystem"],
    )
    supplements__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_supplements", title="Extension field for ``supplements``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this code system (human friendly)",
        description="A short, descriptive, user-friendly title for the code system.",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this code system, represented as a URI "
            "(globally unique) (Coding.system)"
        ),
        description=(
            "An absolute URI that is used to identify this code system when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this code system is (or will be) published. This URL can "
            "be the target of a canonical reference. It SHALL remain the same when "
            "the code system is stored on different servers. This is used in "
            "[Coding](datatypes.html#Coding).system."
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
            "indexing and searching for appropriate code system instances."
        ),
    )

    valueSet: fhirtypes.Canonical = Field(
        None,
        alias="valueSet",
        title="Canonical reference to the value set with entire code system",
        description=(
            "Canonical reference to the value set that contains the entire code "
            "system."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueSet", title="Extension field for ``valueSet``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the code system (Coding.version)",
        description=(
            "The identifier that is used to identify this version of the code "
            "system when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the code system author"
            " and is not expected to be globally unique. For example, it might be a"
            " timestamp (e.g. yyyymmdd) if a managed version is not available. "
            "There is also no expectation that versions can be placed in a "
            "lexicographical sequence. This is used in "
            "[Coding](datatypes.html#Coding).version."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )

    versionNeeded: bool = Field(
        None,
        alias="versionNeeded",
        title="If definitions are not stable",
        description=(
            "This flag is used to signify that the code system does not commit to "
            "concept permanence across versions. If true, a version must be "
            "specified when referencing this code system."
        ),
    )
    versionNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versionNeeded", title="Extension field for ``versionNeeded``."
    )


class CodeSystemConcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Concepts in the code system.
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """

    resource_type = Field("CodeSystemConcept", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Code that identifies concept",
        description=(
            "A code - a text symbol - that uniquely identifies the concept within "
            "the code system."
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    concept: ListType[fhirtypes.CodeSystemConceptType] = Field(
        None,
        alias="concept",
        title="Child Concepts (is-a/contains/categorizes)",
        description=(
            "Defines children of a concept to produce a hierarchy of concepts. The "
            "nature of the relationships is variable (is-a/contains/categorizes) - "
            "see hierarchyMeaning."
        ),
    )

    definition: fhirtypes.String = Field(
        None,
        alias="definition",
        title="Formal definition",
        description=(
            "The formal definition of the concept. The code system resource does "
            "not make formal definitions required, because of the prevalence of "
            "legacy systems. However, they are highly recommended, as without them "
            "there is no formal meaning associated with the concept."
        ),
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    designation: ListType[fhirtypes.CodeSystemConceptDesignationType] = Field(
        None,
        alias="designation",
        title="Additional representations for the concept",
        description=(
            "Additional representations for the concept - other languages, aliases,"
            " specialized purposes, used for particular purposes, etc."
        ),
    )

    display: fhirtypes.String = Field(
        None,
        alias="display",
        title="Text to display to the user",
        description=(
            "A human readable string that is the recommended default way to present"
            " this concept to a user."
        ),
    )
    display__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_display", title="Extension field for ``display``."
    )

    property: ListType[fhirtypes.CodeSystemConceptPropertyType] = Field(
        None,
        alias="property",
        title="Property value for the concept",
        description="A property value for this concept.",
    )


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional representations for the concept.
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """

    resource_type = Field("CodeSystemConceptDesignation", const=True)

    language: fhirtypes.Code = Field(
        None,
        alias="language",
        title="Human language of the designation",
        description="The language this designation is defined for.",
    )
    language__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_language", title="Extension field for ``language``."
    )

    use: fhirtypes.CodingType = Field(
        None,
        alias="use",
        title="Details how this designation would be used",
        description="A code that details how this designation would be used.",
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="The text value for this designation",
        description=None,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Property value for the concept.
    A property value for this concept.
    """

    resource_type = Field("CodeSystemConceptProperty", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Reference to CodeSystem.property.code",
        description="A code that is a reference to CodeSystem.property.code.",
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    valueDateTime: fhirtypes.DateTime = Field(
        None,
        alias="valueDateTime",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.Decimal = Field(
        None,
        alias="valueDecimal",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueInteger: fhirtypes.Integer = Field(
        None,
        alias="valueInteger",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueString: fhirtypes.String = Field(
        None,
        alias="valueString",
        title="Value of the property for this concept",
        description="The value of this property.",
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
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
                "valueCode",
                "valueCoding",
                "valueDateTime",
                "valueDecimal",
                "valueInteger",
                "valueString",
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


class CodeSystemFilter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Filter that can be used in a value set.
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """

    resource_type = Field("CodeSystemFilter", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="Code that identifies the filter",
        description=(
            "The code that identifies this filter when it is used as a filter in "
            "[ValueSet](valueset.html#).compose.include.filter."
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="How or why the filter is used",
        description="A description of how or why the filter is used.",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    operator: ListType[fhirtypes.Code] = Field(
        ...,
        alias="operator",
        title=(
            "= | is-a | descendent-of | is-not-a | regex | in | not-in | "
            "generalizes | exists"
        ),
        description="A list of operators that can be used with the filter.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "=",
            "is-a",
            "descendent-of",
            "is-not-a",
            "regex",
            "in",
            "not-in",
            "generalizes",
            "exists",
        ],
    )
    operator__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_operator", title="Extension field for ``operator``."
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="What to use for the value",
        description="A description of what the value for the filter should be.",
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )


class CodeSystemProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional information supplied about each concept.
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """

    resource_type = Field("CodeSystemProperty", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title=(
            "Identifies the property on the concepts, and when referred to in "
            "operations"
        ),
        description=(
            "A code that is used to identify the property. The code is used "
            "internally (in CodeSystem.concept.property.code) and also externally, "
            "such as in property filters."
        ),
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Why the property is defined, and/or what it conveys",
        description=(
            "A description of the property- why it is defined, and how its value "
            "might be used."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="code | Coding | string | integer | boolean | dateTime | decimal",
        description=(
            'The type of the property value. Properties of type "code" contain a '
            "code defined by the code system (e.g. a reference to another defined "
            "concept)."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "code",
            "Coding",
            "string",
            "integer",
            "boolean",
            "dateTime",
            "decimal",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Formal identifier for the property",
        description=(
            "Reference to the formal meaning of the property. One possible source "
            "of meaning is the [Concept Properties](codesystem-concept-"
            "properties.html) code system."
        ),
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )
