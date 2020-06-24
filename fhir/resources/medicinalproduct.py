# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProduct
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


class MedicinalProduct(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """

    resource_type = Field("MedicinalProduct", const=True)

    additionalMonitoringIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additionalMonitoringIndicator",
        title=(
            "Whether the Medicinal Product is subject to additional monitoring for "
            "regulatory reasons"
        ),
        description=None,
    )

    attachedDocument: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="attachedDocument",
        title="Supporting documentation, typically for regulatory submission",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    clinicalTrial: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="clinicalTrial",
        title="Clinical trials or studies that this product is involved in",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ResearchStudy"],
    )

    combinedPharmaceuticalDoseForm: fhirtypes.CodeableConceptType = Field(
        None,
        alias="combinedPharmaceuticalDoseForm",
        title=(
            "The dose form for a single part product, or combined form of a "
            "multiple part product"
        ),
        description=None,
    )

    contact: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="contact",
        title="A product specific contact, person (in a role), or an organization",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "PractitionerRole"],
    )

    crossReference: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="crossReference",
        title=(
            "Reference to another product, e.g. for linking authorised to "
            "investigational product"
        ),
        description=None,
    )

    domain: fhirtypes.CodingType = Field(
        None,
        alias="domain",
        title="If this medicine applies to human or veterinary uses",
        description=None,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business identifier for this product. Could be an MPID",
        description=None,
    )

    legalStatusOfSupply: fhirtypes.CodeableConceptType = Field(
        None,
        alias="legalStatusOfSupply",
        title=(
            "The legal status of supply of the medicinal product as classified by "
            "the regulator"
        ),
        description=None,
    )

    manufacturingBusinessOperation: ListType[
        fhirtypes.MedicinalProductManufacturingBusinessOperationType
    ] = Field(
        None,
        alias="manufacturingBusinessOperation",
        title=(
            "An operation applied to the product, for manufacturing or "
            "adminsitrative purpose"
        ),
        description=None,
    )

    marketingStatus: ListType[fhirtypes.MarketingStatusType] = Field(
        None,
        alias="marketingStatus",
        title=(
            "Marketing status of the medicinal product, in contrast to marketing "
            "authorizaton"
        ),
        description=None,
    )

    masterFile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="masterFile",
        title=(
            "A master file for to the medicinal product (e.g. Pharmacovigilance "
            "System Master File)"
        ),
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DocumentReference"],
    )

    name: ListType[fhirtypes.MedicinalProductNameType] = Field(
        ...,
        alias="name",
        title="The product's name, including full name and possibly coded parts",
        description=None,
    )

    packagedMedicinalProduct: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="packagedMedicinalProduct",
        title="Package representation for the product",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductPackaged"],
    )

    paediatricUseIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="paediatricUseIndicator",
        title="If authorised for use in children",
        description=None,
    )

    pharmaceuticalProduct: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="pharmaceuticalProduct",
        title="Pharmaceutical aspects of product",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductPharmaceutical"],
    )

    productClassification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="productClassification",
        title="Allows the product to be classified by various systems",
        description=None,
    )

    specialDesignation: ListType[
        fhirtypes.MedicinalProductSpecialDesignationType
    ] = Field(
        None,
        alias="specialDesignation",
        title=(
            "Indicates if the medicinal product has an orphan designation for the "
            "treatment of a rare disease"
        ),
        description=None,
    )

    specialMeasures: ListType[fhirtypes.String] = Field(
        None,
        alias="specialMeasures",
        title=(
            "Whether the Medicinal Product is subject to special measures for "
            "regulatory reasons"
        ),
        description=None,
    )
    specialMeasures__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_specialMeasures", title="Extension field for ``specialMeasures``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Regulatory type, e.g. Investigational or Authorized",
        description=None,
    )


class MedicinalProductManufacturingBusinessOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """

    resource_type = Field("MedicinalProductManufacturingBusinessOperation", const=True)

    authorisationReferenceNumber: fhirtypes.IdentifierType = Field(
        None,
        alias="authorisationReferenceNumber",
        title="Regulatory authorization reference number",
        description=None,
    )

    confidentialityIndicator: fhirtypes.CodeableConceptType = Field(
        None,
        alias="confidentialityIndicator",
        title="To indicate if this proces is commercially confidential",
        description=None,
    )

    effectiveDate: fhirtypes.DateTime = Field(
        None,
        alias="effectiveDate",
        title="Regulatory authorization date",
        description=None,
    )
    effectiveDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_effectiveDate", title="Extension field for ``effectiveDate``."
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title="The manufacturer or establishment associated with the process",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    operationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="operationType",
        title="The type of manufacturing operation",
        description=None,
    )

    regulator: fhirtypes.ReferenceType = Field(
        None,
        alias="regulator",
        title="A regulator which oversees the operation",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )


class MedicinalProductName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The product's name, including full name and possibly coded parts.
    """

    resource_type = Field("MedicinalProductName", const=True)

    countryLanguage: ListType[
        fhirtypes.MedicinalProductNameCountryLanguageType
    ] = Field(
        None,
        alias="countryLanguage",
        title="Country where the name applies",
        description=None,
    )

    namePart: ListType[fhirtypes.MedicinalProductNameNamePartType] = Field(
        None,
        alias="namePart",
        title="Coding words or phrases of the name",
        description=None,
    )

    productName: fhirtypes.String = Field(
        ..., alias="productName", title="The full product name", description=None,
    )
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_productName", title="Extension field for ``productName``."
    )


class MedicinalProductNameCountryLanguage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Country where the name applies.
    """

    resource_type = Field("MedicinalProductNameCountryLanguage", const=True)

    country: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="country",
        title="Country code for where this name applies",
        description=None,
    )

    jurisdiction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="jurisdiction",
        title="Jurisdiction code for where this name applies",
        description=None,
    )

    language: fhirtypes.CodeableConceptType = Field(
        ..., alias="language", title="Language code for this name", description=None,
    )


class MedicinalProductNameNamePart(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Coding words or phrases of the name.
    """

    resource_type = Field("MedicinalProductNameNamePart", const=True)

    part: fhirtypes.String = Field(
        ..., alias="part", title="A fragment of a product name", description=None,
    )
    part__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_part", title="Extension field for ``part``."
    )

    type: fhirtypes.CodingType = Field(
        ...,
        alias="type",
        title="Idenifying type for this part of the name (e.g. strength part)",
        description=None,
    )


class MedicinalProductSpecialDesignation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """

    resource_type = Field("MedicinalProductSpecialDesignation", const=True)

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date when the designation was granted",
        description=None,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifier for the designation, or procedure number",
        description=None,
    )

    indicationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="indicationCodeableConcept",
        title="Condition for which the medicinal use applies",
        description=None,
        # Choice of Data Types. i.e indication[x]
        one_of_many="indication",
        one_of_many_required=False,
    )

    indicationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="indicationReference",
        title="Condition for which the medicinal use applies",
        description=None,
        # Choice of Data Types. i.e indication[x]
        one_of_many="indication",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductIndication"],
    )

    intendedUse: fhirtypes.CodeableConceptType = Field(
        None,
        alias="intendedUse",
        title="The intended use of the product, e.g. prevention, treatment",
        description=None,
    )

    species: fhirtypes.CodeableConceptType = Field(
        None,
        alias="species",
        title="Animal species for which this applies",
        description=None,
    )

    status: fhirtypes.CodeableConceptType = Field(
        None,
        alias="status",
        title="For example granted, pending, expired or withdrawn",
        description=None,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of special designation, e.g. orphan drug, minor use",
        description=None,
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
            "indication": ["indicationCodeableConcept", "indicationReference"]
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
