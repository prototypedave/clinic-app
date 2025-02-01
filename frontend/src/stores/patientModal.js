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
			this.openRegister = false;
		},

		scheduledModal () {
			this.openEmergency = false;
			this.openScheduled = true;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = false;
		},

		managementModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = true;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = false;
		},

		maternityModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = true;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = false;
		},

		rehabilitationModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = true;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = false;
		},

		palliativeModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = true;
			this.openConsultation = false;
			this.openRegister = false;
		},

		consultationModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = true;
			this.openRegister = false;
		},

		registerModal () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = true;
		},

		reset () {
			this.openEmergency = false;
			this.openScheduled = false;
			this.openManagement = false;
			this.openMaternity = false;
			this.openRehabilitation = false;
			this.openPalliative = false;
			this.openConsultation = false;
			this.openRegister = false;
		},

		setId ({ id }) {
			this.setId = id;
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
	},
});