# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Consent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A healthcare consumer's policy choices to permits or denies recipients or
    roles to perform actions for specific purposes and periods of time.
    A record of a healthcare consumer’s policy choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    resource_type = Field("Consent", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="Actions controlled by this consent",
        description=None,
    )

    actor: ListType[fhirtypes.ConsentActorType] = Field(
        None,
        alias="actor",
        title="Who|what controlled by this consent (or group, by role)",
        description=(
            "Who or what is controlled by this consent. Use group to identify a set"
            " of actors by some property they share (e.g. 'admitting officers')."
        ),
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Classification of the consent statement - for indexing/retrieval",
        description=(
            "A classification of the type of consents found in the statement. This "
            "element supports indexing and retrieval of consent statements."
        ),
    )

    consentingParty: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="consentingParty",
        title="Who is agreeing to the policy and exceptions",
        description=(
            "Either the Grantor, which is the entity responsible for granting the "
            "rights listed in a Consent Directive or the Grantee, which is the "
            "entity responsible for complying with the Consent Directive, including"
            " any obligations or limitations on authorizations and enforcement of "
            "prohibitions."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
        ],
    )

    data: ListType[fhirtypes.ConsentDataType] = Field(
        None,
        alias="data",
        title="Data controlled by this consent",
        description=(
            "The resources controlled by this consent, if specific resources are "
            "referenced."
        ),
    )

    dataPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataPeriod",
        title="Timeframe for data controlled by this consent",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this consent."
        ),
    )

    dateTime: fhirtypes.DateTime = Field(
        None,
        alias="dateTime",
        title="When this Consent was created or indexed",
        description="When this  Consent was issued / created / indexed.",
    )
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_dateTime", title="Extension field for ``dateTime``."
    )

    except_fhir: ListType[fhirtypes.ConsentExceptType] = Field(
        None,
        alias="except",
        title="Additional rule -  addition or removal of permissions",
        description=(
            "An exception to the base policy of this consent. An exception can be "
            "an addition or removal of access permissions."
        ),
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Identifier for this record (external references)",
        description="Unique identifier for this copy of the Consent Statement.",
    )

    organization: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="organization",
        title="Custodian of the consent",
        description=(
            "The organization that manages the consent, and the framework within "
            "which it is executed."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="Who the consent applies to",
        description="The patient/healthcare consumer to whom this consent applies.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Period that this consent applies",
        description="Relevant time or time-period when this Consent is applicable.",
    )

    policy: ListType[fhirtypes.ConsentPolicyType] = Field(
        None,
        alias="policy",
        title="Policies covered by this consent",
        description=(
            "The references to the policies that are included in this consent "
            "scope. Policies may be organizational, but are often defined "
            "jurisdictionally, or in law."
        ),
    )

    policyRule: fhirtypes.Uri = Field(
        None,
        alias="policyRule",
        title="Policy that this consents to",
        description="A referece to the specific computable policy.",
    )
    policyRule__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_policyRule", title="Extension field for ``policyRule``."
    )

    purpose: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="purpose",
        title="Context of activities for which the agreement is made",
        description=(
            "The context of the activities a user is taking - why the user is "
            "accessing the data - that are controlled by this consent."
        ),
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="Security Labels that define affected resources",
        description=(
            "A set of security labels that define which resources are controlled by"
            " this consent. If more than one label is specified, all resources must"
            " have all the specified labels."
        ),
    )

    sourceAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="sourceAttachment",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )

    sourceIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="sourceIdentifier",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
    )

    sourceReference: fhirtypes.ReferenceType = Field(
        None,
        alias="sourceReference",
        title="Source from which this consent is taken",
        description=(
            "The source on which this consent statement is based. The source might "
            "be a scanned original paper form, or a reference to a consent that "
            "links back to such a source, a reference to a document repository "
            "(e.g. XDS) that stores the original consent document."
        ),
        # Choice of Data Types. i.e source[x]
        one_of_many="source",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Consent",
            "DocumentReference",
            "Contract",
            "QuestionnaireResponse",
        ],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | proposed | active | rejected | inactive | entered-in-error",
        description="Indicates the current state of this consent.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "draft",
            "proposed",
            "active",
            "rejected",
            "inactive",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
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
            "source": ["sourceAttachment", "sourceIdentifier", "sourceReference"]
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


class ConsentActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who|what controlled by this consent (or group, by role).
    Who or what is controlled by this consent. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = Field("ConsentActor", const=True)

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Resource for the actor (or group, by role)",
        description=(
            "The resource that identifies the actor. To identify a actors by type, "
            "use group to identify a set of actors by some property they share "
            "(e.g. 'admitting officers')."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Group",
            "CareTeam",
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
        ],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="How the actor is involved",
        description=(
            "How the individual is involved in the resources content that is "
            "described in the consent."
        ),
    )


class ConsentData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data controlled by this consent.
    The resources controlled by this consent, if specific resources are
    referenced.
    """

    resource_type = Field("ConsentData", const=True)

    meaning: fhirtypes.Code = Field(
        ...,
        alias="meaning",
        title="instance | related | dependents | authoredby",
        description=(
            "How the resource reference is interpreted when testing consent "
            "restrictions."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "related", "dependents", "authoredby"],
    )
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_meaning", title="Extension field for ``meaning``."
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="The actual data reference",
        description=(
            "A reference to a specific resource that defines which resources are "
            "covered by this consent."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )


class ConsentExcept(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional rule -  addition or removal of permissions.
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    resource_type = Field("ConsentExcept", const=True)

    action: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="action",
        title="Actions controlled by this exception",
        description="Actions controlled by this Exception.",
    )

    actor: ListType[fhirtypes.ConsentExceptActorType] = Field(
        None,
        alias="actor",
        title="Who|what controlled by this exception (or group, by role)",
        description=(
            "Who or what is controlled by this Exception. Use group to identify a "
            "set of actors by some property they share (e.g. 'admitting officers')."
        ),
    )

    class_fhir: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="class",
        title="e.g. Resource Type, Profile, or CDA etc",
        description=(
            "The class of information covered by this exception. The type can be a "
            "FHIR resource type, a profile on a type, or a CDA document, or some "
            "other type that indicates what sort of information the consent relates"
            " to."
        ),
    )

    code: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="code",
        title="e.g. LOINC or SNOMED CT code, etc in the content",
        description="If this code is found in an instance, then the exception applies.",
    )

    data: ListType[fhirtypes.ConsentExceptDataType] = Field(
        None,
        alias="data",
        title="Data controlled by this exception",
        description=(
            "The resources controlled by this exception, if specific resources are "
            "referenced."
        ),
    )

    dataPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="dataPeriod",
        title="Timeframe for data controlled by this exception",
        description=(
            "Clinical or Operational Relevant period of time that bounds the data "
            "controlled by this exception."
        ),
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Timeframe for this exception",
        description="The timeframe in this exception is valid.",
    )

    purpose: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="purpose",
        title="Context of activities covered by this exception",
        description=(
            "The context of the activities a user is taking - why the user is "
            "accessing the data - that are controlled by this exception."
        ),
    )

    securityLabel: ListType[fhirtypes.CodingType] = Field(
        None,
        alias="securityLabel",
        title="Security Labels that define affected resources",
        description=(
            "A set of security labels that define which resources are controlled by"
            " this exception. If more than one label is specified, all resources "
            "must have all the specified labels."
        ),
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="deny | permit",
        description=(
            "Action  to take - permit or deny - when the exception conditions are "
            "met."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["deny", "permit"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class ConsentExceptActor(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who|what controlled by this exception (or group, by role).
    Who or what is controlled by this Exception. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = Field("ConsentExceptActor", const=True)

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="Resource for the actor (or group, by role)",
        description=(
            "The resource that identifies the actor. To identify a actors by type, "
            "use group to identify a set of actors by some property they share "
            "(e.g. 'admitting officers')."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Group",
            "CareTeam",
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
        ],
    )

    role: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="role",
        title="How the actor is involved",
        description=(
            "How the individual is involved in the resources content that is "
            "described in the exception."
        ),
    )


class ConsentExceptData(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data controlled by this exception.
    The resources controlled by this exception, if specific resources are
    referenced.
    """

    resource_type = Field("ConsentExceptData", const=True)

    meaning: fhirtypes.Code = Field(
        ...,
        alias="meaning",
        title="instance | related | dependents | authoredby",
        description=(
            "How the resource reference is interpreted when testing consent "
            "restrictions."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "related", "dependents", "authoredby"],
    )
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_meaning", title="Extension field for ``meaning``."
    )

    reference: fhirtypes.ReferenceType = Field(
        ...,
        alias="reference",
        title="The actual data reference",
        description=(
            "A reference to a specific resource that defines which resources are "
            "covered by this consent."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )


class ConsentPolicy(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Policies covered by this consent.
    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """

    resource_type = Field("ConsentPolicy", const=True)

    authority: fhirtypes.Uri = Field(
        None,
        alias="authority",
        title="Enforcement source for policy",
        description=(
            "Entity or Organization having regulatory jurisdiction or "
            "accountability for \u00a0enforcing policies pertaining to Consent "
            "Directives."
        ),
    )
    authority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_authority", title="Extension field for ``authority``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Specific policy covered by this consent",
        description=(
            "The references to the policies that are included in this consent "
            "scope. Policies may be organizational, but are often defined "
            "jurisdictionally, or in law."
        ),
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )
