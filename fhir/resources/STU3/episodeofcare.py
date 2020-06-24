# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class EpisodeOfCare(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """

    resource_type = Field("EpisodeOfCare", const=True)

    account: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title=(
            "The set of accounts that may be used for billing for this " "EpisodeOfCare"
        ),
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Account"],
    )

    careManager: fhirtypes.ReferenceType = Field(
        None,
        alias="careManager",
        title="Care manager/care co-ordinator for the patient",
        description=(
            "The practitioner that is the care manager/care co-ordinator for this "
            "patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    diagnosis: ListType[fhirtypes.EpisodeOfCareDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="The list of diagnosis relevant to this episode of care",
        description=None,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier(s) relevant for this EpisodeOfCare",
        description=(
            "The EpisodeOfCare may be known by different identifiers for different "
            "contexts of use, such as when an external agency is tracking the "
            "Episode for funding purposes."
        ),
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization that assumes care",
        description=(
            "The organization that has assumed the specific responsibilities for "
            "the specified duration."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="The patient who is the focus of this episode of care",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Interval during responsibility is assumed",
        description=(
            "The interval during which the managing organization assumes the "
            "defined responsibility."
        ),
    )

    referralRequest: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="referralRequest",
        title="Originating Referral Request(s)",
        description=(
            "Referral Request(s) that are fulfilled by this EpisodeOfCare, incoming"
            " referrals."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ReferralRequest"],
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
        description="planned | waitlist | active | onhold | finished | cancelled.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "waitlist",
            "active",
            "onhold",
            "finished",
            "cancelled",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusHistory: ListType[fhirtypes.EpisodeOfCareStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title=(
            "Past list of status codes (the current status may be included to cover"
            " the start date of the status)"
        ),
        description=(
            "The history of statuses that the EpisodeOfCare has been through "
            "(without requiring processing the history of the resource)."
        ),
    )

    team: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="team",
        title="Other practitioners facilitating this episode of care",
        description=(
            "The list of practitioners that may be facilitating this episode of "
            "care for specific purposes."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CareTeam"],
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type/class  - e.g. specialist referral, disease management",
        description=(
            "A classification of the type of episode of care; e.g. specialist "
            "referral, disease management, type of funded care."
        ),
    )


class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The list of diagnosis relevant to this episode of care.
    """

    resource_type = Field("EpisodeOfCareDiagnosis", const=True)

    condition: fhirtypes.ReferenceType = Field(
        ...,
        alias="condition",
        title="Conditions/problems/diagnoses this episode of care is for",
        description=(
            "A list of conditions/problems/diagnoses that this episode of care is "
            "intended to be providing care for."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition"],
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Ranking of the diagnosis (for each role type)",
        description=None,
    )
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_rank", title="Extension field for ``rank``."
    )

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title=(
            "Role that this diagnosis has within the episode of care (e.g. "
            "admission, billing, discharge \u2026)"
        ),
        description=None,
    )


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Past list of status codes (the current status may be included to cover the
    start date of the status).
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """

    resource_type = Field("EpisodeOfCareStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Duration the EpisodeOfCare was in the specified status",
        description="The period during this EpisodeOfCare that the specific status applied.",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "planned | waitlist | active | onhold | finished | cancelled | entered-"
            "in-error"
        ),
        description="planned | waitlist | active | onhold | finished | cancelled.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "planned",
            "waitlist",
            "active",
            "onhold",
            "finished",
            "cancelled",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )
