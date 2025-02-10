import { defineStore } from 'pinia';
export const usePatientModalStore = defineStore('patientModal', {
	state: () => ({
		openEmergency: false,
		openScheduled: false,
		openManagement: false,
		openMaternity: false,
		openRehabilitation: false,
		openPalliative: false,
		openConsultation: false,
		openRegister: false,
		id: null,
		vitals: false,
		medicationManagement: false,
	}),
	actions: {
		reset () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = false;
			this.vitals = false
			this.medicationManagement = false
		},

		emergencyModal () {
			this.openEmergency = true;
		},

		scheduledModal () {
			this.openScheduled = true;
		},

		managementModal () {
			this.openManagement = true;
		},

		maternityModal () {
			this.openMaternity = true;
		},

		rehabilitationModal () {
			this.openRehabilitation = true;
		},

		palliativeModal () {
			this.openPalliative = true;
		},

		consultationModal () {
			this.openConsultation = true;
		},

		registerModal () {
			this.openRegister = true;
		},

		vitalModal () {
			this.vitals = true;
		},

		medicationManagementModal () {
			this.medicationManagement = true;
		},

		setId ({ id }) {
			this.id = id;
		}
	},
	getters: {
		getEmergency: (state) => state.openEmergency,
		getScheduled: (state) => state.openScheduled,
		getManagement: (state) => state.openManagement,
		getMaternity: (state) => state.openMaternity,
		getRehabilitation: (state) => state.openRehabilitation,
		getPalliative: (state) => state.openPalliative,
		getConsultation: (state) => state.openConsultation,
		getRegister: (state) => state.openRegister,
		getId: (state) => state.id,
		getVitals: (state) => state.vitals,
		getMedicationManagement: (state) => state.medicationManagement,
	},
});