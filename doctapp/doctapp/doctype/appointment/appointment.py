# Copyright (c) 2025, sabbir and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Appointment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		clinic: DF.Link
		contact_number: DF.Data | None
		date: DF.Date
		patient_name: DF.Data
		queue_number: DF.Int
	# end: auto-generated types

	pass
