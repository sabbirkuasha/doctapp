# Copyright (c) 2025, sabbir and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Doctor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from doctapp.doctapp.doctype.doctor_shift.doctor_shift import DoctorShift
		from frappe.types import DF

		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data | None
		qualification: DF.Data | None
		speciality: DF.Data
		table_gocb: DF.Table[DoctorShift]
	# end: auto-generated types

	def validate(self):
		self.set_full_name()
		pass

	def set_full_name(self):
		"""
        Sets the full name of the doctor based on first and last names.
        Handles cases where the last name might be missing.
        """
		# Plain Simple Logic
		# self.full_name = self.first_name + ' ' + self.last_name
		
		# Handle if last name not present
		self.full_name = (
			(self.first_name + ' ' + self.last_name) if self.last_name else self.first_name
			)
	pass

