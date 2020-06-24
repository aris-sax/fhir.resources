# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EligibilityResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class EligibilityResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    EligibilityResponse resource.
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """

    resource_type = Field("EligibilityResponse", const=True)

    created: fhirtypes.DateTime = Field(
        None,
        alias="created",
        title="Creation date",
        description=(
            "The date when the enclosed suite of services were performed or "
            "completed."
        ),
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    disposition: fhirtypes.String = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A description of the status of the adjudication.",
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    error: ListType[fhirtypes.EligibilityResponseErrorType] = Field(
        None,
        alias="error",
        title="Processing errors",
        description="Mutually exclusive with Services Provided (Item).",
    )

    form: fhirtypes.CodeableConceptType = Field(
        None,
        alias="form",
        title="Printed Form Identifier",
        description="The form to be used for printing the content.",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
    )

    inforce: bool = Field(
        None,
        alias="inforce",
        title="Coverage inforce indicator",
        description=(
            "Flag indicating if the coverage provided is inforce currently  if no "
            "service date(s) specified or for the whole duration of the service "
            "dates."
        ),
    )
    inforce__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_inforce", title="Extension field for ``inforce``."
    )

    insurance: ListType[fhirtypes.EligibilityResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title="Details by insurance coverage",
        description=(
            "The insurer may provide both the details for the requested coverage as"
            " well as details for additional coverages known to the insurer."
        ),
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Insurer issuing the coverage",
        description="The Insurer who produced this adjudicated response.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    outcome: fhirtypes.CodeableConceptType = Field(
        None,
        alias="outcome",
        title="complete | error | partial",
        description="Transaction status: error, complete.",
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Eligibility reference",
        description="Original request resource reference.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["EligibilityRequest"],
    )

    requestOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="requestOrganization",
        title="Responsible organization",
        description=(
            "The organization which is responsible for the services rendered to the"
            " patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    requestProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="requestProvider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
            "patient."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "cancelled", "draft", "entered-in-error"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )


class EligibilityResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Mutually exclusive with Services Provided (Item).
    """

    resource_type = Field("EligibilityResponseError", const=True)

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code,from a specified code system, which details why the "
            "eligibility check could not be performed."
        ),
    )


class EligibilityResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details by insurance coverage.
    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """

    resource_type = Field("EligibilityResponseInsurance", const=True)

    benefitBalance: ListType[
        fhirtypes.EligibilityResponseInsuranceBenefitBalanceType
    ] = Field(
        None,
        alias="benefitBalance",
        title="Benefits by Category",
        description="Benefits and optionally current balances by Category.",
    )

    contract: fhirtypes.ReferenceType = Field(
        None,
        alias="contract",
        title="Contract details",
        description="The contract resource which may provide more detailed information.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Contract"],
    )

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title="Updated Coverage details",
        description="A suite of updated or additional Coverages from the Insurer.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Coverage"],
    )


class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefits by Category.
    Benefits and optionally current balances by Category.
    """

    resource_type = Field("EligibilityResponseInsuranceBenefitBalance", const=True)

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type of services covered",
        description="Dental, Vision, Medical, Pharmacy, Rehab etc.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Description of the benefit or services covered",
        description=(
            "A richer description of the benefit, for example 'DENT2 covers 100% of"
            " basic, 50% of major but exclused Ortho, Implants and Costmetic "
            "services'."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    excluded: bool = Field(
        None,
        alias="excluded",
        title="Excluded from the plan",
        description=(
            "True if the indicated class of service is excluded from the plan, "
            "missing or False indicated the service is included in the coverage."
        ),
    )
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_excluded", title="Extension field for ``excluded``."
    )

    financial: ListType[
        fhirtypes.EligibilityResponseInsuranceBenefitBalanceFinancialType
    ] = Field(
        None,
        alias="financial",
        title="Benefit Summary",
        description="Benefits Used to date.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Short name for the benefit",
        description="A short name or tag for the benefit, for example MED01, or DENT2.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.CodeableConceptType = Field(
        None,
        alias="network",
        title="In or out of network",
        description="Network designation.",
    )

    subCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subCategory",
        title="Detailed services covered within the type",
        description="Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.",
    )

    term: fhirtypes.CodeableConceptType = Field(
        None,
        alias="term",
        title="Annual or lifetime",
        description=(
            "The term or period of the values such as 'maximum lifetime benefit' or"
            " 'maximum annual vistis'."
        ),
    )

    unit: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unit",
        title="Individual or family",
        description="Unit designation: individual or family.",
    )


class EligibilityResponseInsuranceBenefitBalanceFinancial(
    backboneelement.BackboneElement
):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Benefit Summary.
    Benefits Used to date.
    """

    resource_type = Field(
        "EligibilityResponseInsuranceBenefitBalanceFinancial", const=True
    )

    allowedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="allowedMoney",
        title="Benefits allowed",
        description=None,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )

    allowedString: fhirtypes.String = Field(
        None,
        alias="allowedString",
        title="Benefits allowed",
        description=None,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allowedString", title="Extension field for ``allowedString``."
    )

    allowedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="allowedUnsignedInt",
        title="Benefits allowed",
        description=None,
        # Choice of Data Types. i.e allowed[x]
        one_of_many="allowed",
        one_of_many_required=False,
    )
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_allowedUnsignedInt",
        title="Extension field for ``allowedUnsignedInt``.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        ..., alias="type", title="Deductable, visits, benefit amount", description=None,
    )

    usedMoney: fhirtypes.MoneyType = Field(
        None,
        alias="usedMoney",
        title="Benefits used",
        description=None,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )

    usedUnsignedInt: fhirtypes.UnsignedInt = Field(
        None,
        alias="usedUnsignedInt",
        title="Benefits used",
        description=None,
        # Choice of Data Types. i.e used[x]
        one_of_many="used",
        one_of_many_required=False,
    )
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usedUnsignedInt", title="Extension field for ``usedUnsignedInt``."
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
            "allowed": ["allowedMoney", "allowedString", "allowedUnsignedInt"],
            "used": ["usedMoney", "usedUnsignedInt"],
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
