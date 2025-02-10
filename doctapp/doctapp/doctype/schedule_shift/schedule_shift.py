# Copyright (c) 2025, sabbir and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ScheduleShift(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		clinic: DF.Link
		endtime: DF.Time
		starttime: DF.Time
		title: DF.Data | None
	# end: auto-generated types

	pass
