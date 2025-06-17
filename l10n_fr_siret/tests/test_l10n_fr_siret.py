from odoo.exceptions import ValidationError  # type: ignore[import-untyped]
from odoo.tests import TransactionCase  # type: ignore[import-untyped]


class Test(TransactionCase):
    """Test SIRET."""

    def test_invalid_siret(self):
        """Ensure checks operate normally when updating the SIRET."""

        with self.assertRaisesRegex(
            ValidationError,
            "The NIC '0001' is incorrect: it must have exactly 5 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "5555555560001"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The NIC '0001A' is incorrect: it must have exactly 5 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "55555555600011"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIREN '55555555' is incorrect: it must have exactly 9 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "555555556"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIREN '55555555C' is incorrect: it must have exactly 9 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "55555555C"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIREN '555555559' is invalid: the checksum is wrong.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner B", "siret": "555555559"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIRET '55555555600012' is invalid: the checksum is wrong.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner B", "siret": "55555555600012"}
            )
