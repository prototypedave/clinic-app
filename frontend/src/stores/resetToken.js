import { defineStore } from 'pinia';

export const useTokenStore = defineStore('resetToken', {
	state: () => ({
		resetToken: null,
	}), 
	actions: {
		saveResetToken (token) {
			this.resetToken = token;
		}
	},
	getters: {
		token: (state) => state.resetToken,
	}
});