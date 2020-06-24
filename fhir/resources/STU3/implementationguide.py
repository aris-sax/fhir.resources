# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class ImplementationGuide(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of rules about how FHIR is used.
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole and to publish a computable definition of all the parts.
    """

    resource_type = Field("ImplementationGuide", const=True)

    binary: ListType[fhirtypes.Uri] = Field(
        None,
        alias="binary",
        title="Image, css, script, etc.",
        description=(
            "A binary file that is included in the  implementation guide when it is"
            " published."
        ),
    )
    binary__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_binary", title="Extension field for ``binary``."
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
            "A copyright statement relating to the implementation guide and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the implementation guide."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the implementation guide was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the implementation "
            "guide changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    dependency: ListType[fhirtypes.ImplementationGuideDependencyType] = Field(
        None,
        alias="dependency",
        title="Another Implementation guide this depends on",
        description=(
            "Another implementation guide that this implementation depends on. "
            "Typically, an implementation guide uses value sets, profiles "
            "etc.defined in other implementation guides."
        ),
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the implementation guide",
        description=(
            "A free text natural language description of the implementation guide "
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
            "A boolean value to indicate that this implementation guide is authored"
            " for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Id = Field(
        None,
        alias="fhirVersion",
        title="FHIR Version this Implementation Guide targets",
        description=(
            "The version of the FHIR specification on which this "
            "ImplementationGuide is based - this is the formal version of the "
            "specification, without the revision number, e.g. "
            "[publication].[major].[minor], which is 3.0.2 for this version."
        ),
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    global_fhir: ListType[fhirtypes.ImplementationGuideGlobalType] = Field(
        None,
        alias="global",
        title="Profiles that apply globally",
        description=(
            "A set of profiles that all resources covered by this implementation "
            "guide must conform to."
        ),
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for implementation guide (if applicable)",
        description=(
            "A legal or geographic region in which the implementation guide is "
            "intended to be used."
        ),
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this implementation guide (computer friendly)",
        description=(
            "A natural language name identifying the implementation guide. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    package: ListType[fhirtypes.ImplementationGuidePackageType] = Field(
        None,
        alias="package",
        title="Group of resources as used in .page.package",
        description=(
            "A logical group of resources. Logical groups can be used when building"
            " pages."
        ),
    )

    page: fhirtypes.ImplementationGuidePageType = Field(
        None,
        alias="page",
        title="Page/Section in the Guide",
        description=(
            "A page / section in the implementation guide. The root page is the "
            "implementation guide home page."
        ),
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "implementation guide."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this implementation guide. Enables tracking the life-"
            "cycle of the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    url: fhirtypes.Uri = Field(
        ...,
        alias="url",
        title="Logical URI to reference this implementation guide (globally unique)",
        description=(
            "An absolute URI that is used to identify this implementation guide "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this implementation guide is (or will be) "
            "published. The URL SHOULD include the major version of the "
            "implementation guide. For more information see [Technical and Business"
            " Versions](resource.html#versions)."
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate implementation guide instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the implementation guide",
        description=(
            "The identifier that is used to identify this version of the "
            "implementation guide when it is referenced in a specification, model, "
            "design or instance. This is an arbitrary value managed by the "
            "implementation guide author and is not expected to be globally unique."
            " For example, it might be a timestamp (e.g. yyyymmdd) if a managed "
            "version is not available. There is also no expectation that versions "
            "can be placed in a lexicographical sequence."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Another Implementation guide this depends on.
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    resource_type = Field("ImplementationGuideDependency", const=True)

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="reference | inclusion",
        description="How the dependency is represented when the guide is published.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["reference", "inclusion"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    uri: fhirtypes.Uri = Field(
        ...,
        alias="uri",
        title="Where to find dependency",
        description="Where the dependency is located.",
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Profiles that apply globally.
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = Field("ImplementationGuideGlobal", const=True)

    profile: fhirtypes.ReferenceType = Field(
        ...,
        alias="profile",
        title="Profile that all resources must conform to",
        description="A reference to the profile that all instances must conform to.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="Type this profiles applies to",
        description="The type of resource that all instances must conform to.",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Group of resources as used in .page.package.
    A logical group of resources. Logical groups can be used when building
    pages.
    """

    resource_type = Field("ImplementationGuidePackage", const=True)

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Human readable text describing the package",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name used .page.package",
        description="The name for the group, as used in page.package.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    resource: ListType[fhirtypes.ImplementationGuidePackageResourceType] = Field(
        ...,
        alias="resource",
        title="Resource in the implementation guide",
        description=(
            "A resource that is part of the implementation guide. Conformance "
            "resources (value set, structure definition, capability statements "
            "etc.) are obvious candidates for inclusion, but any kind of resource "
            "can be included as an example resource."
        ),
    )


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource in the implementation guide.
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = Field("ImplementationGuidePackageResource", const=True)

    acronym: fhirtypes.String = Field(
        None,
        alias="acronym",
        title="Short code to identify the resource",
        description=(
            "A short code that may be used to identify the resource throughout the "
            "implementation guide."
        ),
    )
    acronym__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_acronym", title="Extension field for ``acronym``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Reason why included in guide",
        description=(
            "A description of the reason that a resource has been included in the "
            "implementation guide."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    example: bool = Field(
        ...,
        alias="example",
        title="If not an example, has its normal meaning",
        description=(
            "Whether a resource is included in the guide as part of the rules "
            "defined by the guide, or just as an example of a resource that "
            "conforms to the rules and/or help implementers understand the intent "
            "of the guide."
        ),
    )
    example__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_example", title="Extension field for ``example``."
    )

    exampleFor: fhirtypes.ReferenceType = Field(
        None,
        alias="exampleFor",
        title="Resource this is an example of (if applicable)",
        description=(
            "Another resource that this resource is an example for. This is mostly "
            "used for resources that are included as examples of "
            "StructureDefinitions."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Human Name for the resource",
        description=(
            "A human assigned name for the resource. All resources SHOULD have a "
            "name, but the name may be extracted from the resource (e.g. "
            "ValueSet.name)."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title="Location of the resource",
        description="Where this resource is found.",
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    sourceUri: fhirtypes.Uri = Field(
        None,
        alias="sourceUri",
        title="Location of the resource",
        description="Where this resource is found.",
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=True,
    )
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sourceUri", title="Extension field for ``sourceUri``."
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
        one_of_many_fields = {"source": ["sourceReference", "sourceUri"]}
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


class ImplementationGuidePage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Page/Section in the Guide.
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = Field("ImplementationGuidePage", const=True)

    format: fhirtypes.Code = Field(
        None,
        alias="format",
        title="Format of the page (e.g. html, markdown, etc.)",
        description="The format of the page.",
    )
    format__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_format", title="Extension field for ``format``."
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title=(
            "page | example | list | include | directory | dictionary | toc | "
            "resource"
        ),
        description=(
            "The kind of page that this is. Some pages are autogenerated (list, "
            "example), and other kinds are of interest so that tools can navigate "
            "the user to the page of interest."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "page",
            "example",
            "list",
            "include",
            "directory",
            "dictionary",
            "toc",
            "resource",
        ],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    package: ListType[fhirtypes.String] = Field(
        None,
        alias="package",
        title="Name of package to include",
        description=(
            "For constructed pages, a list of packages to include in the page (or "
            "else empty for everything)."
        ),
    )
    package__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_package", title="Extension field for ``package``."
    )

    page: ListType[fhirtypes.ImplementationGuidePageType] = Field(
        None,
        alias="page",
        title="Nested Pages / Sections",
        description="Nested Pages/Sections under this page.",
    )

    source: fhirtypes.Uri = Field(
        ...,
        alias="source",
        title="Where to find that page",
        description="The source address for the page.",
    )
    source__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_source", title="Extension field for ``source``."
    )

    title: fhirtypes.String = Field(
        ...,
        alias="title",
        title="Short title shown for navigational assistance",
        description=(
            "A short title used to represent this page in navigational structures "
            "such as table of contents, bread crumbs, etc."
        ),
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    type: ListType[fhirtypes.Code] = Field(
        None,
        alias="type",
        title="Kind of resource to include in the list",
        description="For constructed pages, what kind of resources to include in the list.",
    )
    type__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
