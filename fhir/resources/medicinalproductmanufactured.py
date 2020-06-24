# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class MedicinalProductManufactured(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The manufactured item as contained in the packaged medicinal product.
    """

    resource_type = Field("MedicinalProductManufactured", const=True)

    ingredient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="ingredient",
        title="Ingredient",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MedicinalProductIngredient"],
    )

    manufacturedDoseForm: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="manufacturedDoseForm",
        title=(
            "Dose form as manufactured and before any transformation into the "
            "pharmaceutical product"
        ),
        description=None,
    )

    manufacturer: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="manufacturer",
        title=(
            "Manufacturer of the item (Note that this should be named "
            '"manufacturer" but it currently causes technical issues)'
        ),
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    otherCharacteristics: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="otherCharacteristics",
        title="Other codeable characteristics",
        description=None,
    )

    physicalCharacteristics: fhirtypes.ProdCharacteristicType = Field(
        None,
        alias="physicalCharacteristics",
        title="Dimensions, color etc.",
        description="Dimensions, color etc.",
    )

    quantity: fhirtypes.QuantityType = Field(
        ...,
        alias="quantity",
        title='The quantity or "count number" of the manufactured item',
        description=None,
    )

    unitOfPresentation: fhirtypes.CodeableConceptType = Field(
        None,
        alias="unitOfPresentation",
        title=(
            "The \u201creal world\u201d units in which the quantity of the manufactured item "
            "is described"
        ),
        description=None,
    )
