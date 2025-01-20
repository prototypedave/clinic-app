import { defineStore } from 'pinia';

export const useTokenStore = defineStore('resetToken', {
	state: () => ({
		resetToken: null,
	}), 
	actions: {
		saveResetToken (token) {
			this.resetToken = token;
		},
		clearResetToken() {
			this.resetToken = null;
		},
	},
	getters: {
		token: (state) => state.resetToken,
	}
});