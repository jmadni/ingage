
var client;
$(document).ready(async function () {

	const msalConfig = {
		auth: {
			clientId: "51d7c325-0c70-4896-8e8d-140eba1f9d2e", // Client Id of the registered application
			redirectUri: "http://localhost:56802/",
		},
		cache: {
			cacheLocation: "sessionStorage", // This configures where your cache will be stored
			storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge
			forceRefresh: false
		}
	};
	const graphScopes = ["user.read", "Notes.Create", "Notes.Read", "Notes.ReadWrite"]; // An array of graph scopes

	const msalApplication = new Msal.UserAgentApplication(msalConfig);
	const options = new MicrosoftGraph.MSALAuthenticationProviderOptions(graphScopes);
	const authProvider = new MicrosoftGraph.ImplicitMSALAuthenticationProvider(msalApplication, options);

	const providerOptions = {
		authProvider, // An instance created from previous step
	};
	const Client = MicrosoftGraph.Client;
	client = Client.initWithMiddleware(providerOptions);

	try {
		userDetails = await client.api("/me").get();
		console.log(userDetails);
		$("#username").html(userDetails.displayName);

		if (callBack) {
			callBack();
		}
	} catch (error) {
		throw error;
	}
});