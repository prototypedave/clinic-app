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
	}),
	actions: {
		emergencyModal () {
			this.openEmergency = true;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
		},

		scheduledModal () {
			this.openEmergency = false;
			this.openScheduled = true;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
		},

		managementModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = true;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
		},

		maternityModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = true;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
		},

		rehabilitationModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = true;
			this.openPalliative = false;
			this.openConsultation = false;
		},

		palliativeModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = true;
			this.openConsultation = false;
		},

		consultationModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = true;
		},
	},
	getters: {
		getEmergency: (state) => state.openEmergency,
		getScheduled: (state) => state.openScheduled,
		getManagement: (state) => state.openManagement,
		getMaternity: (state) => state.openMaternity,
		getRehabilitation: (state) => state.openRehabilitation,
		getPalliative: (state) => state.openPalliative,
		getConsultation: (state) => state.openConsultation,
	},
});