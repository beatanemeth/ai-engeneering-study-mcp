import { ok, badRequest } from 'wix-http-functions';
import {
	validateAuthorizationHeader,
	decodeJwtToken,
	WIX_AUTH_SECRET,
} from 'backend/util.web';
import {
	yourFindEventsServiceFunction,
	yourFindBlogPostsServiceFunction,
	yourFindBlogCategoriesServiceFunction,
	yourFindBlogTagsServiceFunction,
	yourFindCollectionServiceFunction,
	yourFindMembersServiceFunction,
} from 'backend/services.web';

const ENDPOINT_FIND_EVENTS = 'get_REPLACE_ME_EVENTS_ENDPOINT';
const ENDPOINT_FIND_BLOG_POSTS = 'get_REPLACE_ME_BLOG_POSTS_ENDPOINT';
const ENDPOINT_FIND_COLLECTION = 'get_REPLACE_ME_COLLECTION_ENDPOINT';
const ENDPOINT_FIND_BLOG_TAXONOMIES = 'get_REPLACE_ME_BLOG_TAXONOMIES_ENDPOINT';
const ENDPOINT_FIND_MEMBERS = 'get_REPLACE_ME_MEMBERS_ENDPOINT';

const EXPECTED_JWT_SUB_EVENTS = 'REPLACE-ME-EVENTS-JWT-SUB';
const EXPECTED_JWT_SUB_BLOG_POSTS = 'REPLACE-ME-BLOG-POSTS-JWT-SUB';
const EXPECTED_JWT_SUB_COLLECTION = 'REPLACE-ME-COLLECTION-JWT-SUB';
const EXPECTED_JWT_SUB_BLOG_TAXONOMIES = 'REPLACE-ME-BLOG-TAXONOMIES-JWT-SUB';
const EXPECTED_JWT_SUB_MEMBERS = 'REPLACE-ME-MEMBERS-JWT-SUB';

/**
 * HTTP Function: get_yourEventsEndpoint
 * Endpoint: https://www.yourdomain.com/_functions/yourEventsEndpoint
 *
 * @accepts GET with JSON body:
 * @requires Authorization header: `Bearer YOUR_JWT_TOKEN`
 * @returns {object} Events data (array of events objects) if successful, or an error object.
 */
export async function get_yourEventsEndpoint(request) {
	const response = { headers: { 'Content-Type': 'application/json' } };

	const options = {
		fields: ['CATEGORIES', 'DASHBOARD', 'TEXTS', 'URLS'],
	};

	try {
		const actualToken = validateAuthorizationHeader(
			request,
			ENDPOINT_FIND_EVENTS
		);

		const decodedJwt = await decodeJwtToken(
			actualToken,
			WIX_AUTH_SECRET,
			EXPECTED_JWT_SUB_EVENTS,
			ENDPOINT_FIND_EVENTS
		);

		console.log('DEBUG: Actual Token: ', actualToken);
		console.log('DEBUG: Decoded JWT: ', decodedJwt);

		if (!decodedJwt) {
			console.error(`❌ [${ENDPOINT_FIND_EVENTS}]: Invalid or missing JWT.`);
			response.body = { error: 'Unauthorized: Invalid token.' };
			return badRequest(response);
		}

		const eventsResult = await yourFindEventsServiceFunction(options);

		console.log(
			`🌐 [${ENDPOINT_FIND_EVENTS}]: Received events: `,
			eventsResult.length ?? 0
		);

		response.body = eventsResult;
		return ok(response);
	} catch (error) {
		console.error(
			`❌ [${ENDPOINT_FIND_EVENTS}]: Unexpected error caught: `,
			error
		);
		response.body = { error: error?.message || String(error) };
		return badRequest(response);
	}
}

/**
 * HTTP Function: get_yourBlogPostsEndpoint
 * Endpoint: https://www.yourdomain.com/_functions/yourBlogPostsEndpoint
 *
 * @accepts GET with JSON body:
 * @requires Authorization header: `Bearer YOUR_JWT_TOKEN`
 * @returns {object} Posts data (array of posts objects) if successful, or an error object.
 */
export async function get_yourBlogPostsEndpoint(request) {
	const response = { headers: { 'Content-Type': 'application/json' } };

	const options = {
		fieldsets: ['CONTENT_TEXT', 'URL', 'METRICS'],
	};

	try {
		const actualToken = validateAuthorizationHeader(
			request,
			ENDPOINT_FIND_POSTS
		);

		const decodedJwt = await decodeJwtToken(
			actualToken,
			WIX_AUTH_SECRET,
			EXPECTED_JWT_SUB_BLOG_POSTS,
			ENDPOINT_FIND_BLOG_POSTS
		);

		console.log('DEBUG: Actual Token: ', actualToken);
		console.log('DEBUG: Decoded JWT: ', decodedJwt);

		if (!decodedJwt) {
			console.error(
				`❌ [${ENDPOINT_FIND_BLOG_POSTS}]: Invalid or missing JWT.`
			);
			response.body = { error: 'Unauthorized: Invalid token.' };
			return badRequest(response);
		}

		const postsResult = await yourFindBlogPostsServiceFunction(options);

		console.log(
			`🌐 [${ENDPOINT_FIND_BLOG_POSTS}]: Received posts: `,
			postsResult.length ?? 0
		);

		response.body = postsResult;
		return ok(response);
	} catch (error) {
		console.error(
			`❌ [${ENDPOINT_FIND_BLOG_POSTS}]: Unexpected error caught: `,
			error
		);
		response.body = { error: error?.message || String(error) };
		return badRequest(response);
	}
}

/**
 * HTTP Function: get_yourBlogTaxonomiesEndpoint
 * Endpoint: https://www.kiutarakbol.hu/_functions/yourBlogTaxonomiesEndpoint
 * Results vary based on the queried taxonomy parameter passed (either 'categories' or 'tags').
 * 	.../yourBlogTaxonomiesEndpoint?type=categories
 * 	.../yourBlogTaxonomiesEndpoint?type=tags
 *
 * @accepts GET with JSON body:
 * @requires Authorization header: `Bearer YOUR_JWT_TOKEN`
 * @returns {object} Blog categories or tags data if successful, or an error object.
 */
export async function get_findBlogTaxonomies(request) {
	const response = { headers: { 'Content-Type': 'application/json' } };

	const TAXONOMY_CATEGORIES = 'categories';
	const TAXONOMY_TAGS = 'tags';

	const requestedTaxonomy = request.query.tax;

	if (!requestedTaxonomy) {
		response.body = { error: 'Missing taxonomy name.' };
		return badRequest(response);
	}

	let taxonomyResult = [];

	try {
		const actualToken = validateAuthorizationHeader(
			request,
			ENDPOINT_FIND_BLOG_TAXONOMIES
		);

		const decodedJwt = await decodeJwtToken(
			actualToken,
			WIX_AUTH_SECRET,
			EXPECTED_JWT_SUB_BLOG_TAXONOMIES,
			ENDPOINT_FIND_BLOG_TAXONOMIES
		);

		console.log('DEBUG: Actual Token: ', actualToken);
		console.log('DEBUG: Decoded JWT: ', decodedJwt);

		if (!decodedJwt) {
			console.error(
				`❌ [${ENDPOINT_FIND_BLOG_TAXONOMIES}]: Invalid or missing JWT.`
			);
			response.body = { error: 'Unauthorized: Invalid token.' };
			return badRequest(response);
		}

		if (requestedTaxonomy === TAXONOMY_CATEGORIES) {
			taxonomyResult = await yourFindBlogCategoriesServiceFunction();
		} else if (requestedTaxonomy === TAXONOMY_TAGS) {
			taxonomyResult = await yourFindBlogTagsServiceFunction();
		} else {
			// Handle cases where an unknown ID is passed
			response.body = { error: 'Invalid taxonomy name.' };
			return badRequest(response);
		}

		console.log(
			`🌐 [${ENDPOINT_FIND_BLOG_TAXONOMIES}]: Received taxonomy items: `,
			taxonomyResult.length ?? 0
		);

		response.body = taxonomyResult;
		return ok(response);
	} catch (error) {
		console.error(
			`❌ [${ENDPOINT_FIND_BLOG_TAXONOMIES}]: Unexpected error caught: `,
			error
		);
		response.body = { error: error?.message || String(error) };
		return badRequest(response);
	}
}

/**
 * HTTP Function: get_yourCollectionEndpoint
 * Endpoint: https://www.yourdomain.com/_functions/yourCollectionEndpoint
 * Results vary based on the queried collection parameter passed (either 'articles' or 'articles-categories').
 * 	.../fyourCollectionEndpoint?coll=articles
 * 	.../fyourCollectionEndpoint?coll=articles-categories
 *
 * @accepts GET with JSON body:
 * @requires Authorization header: `Bearer YOUR_JWT_TOKEN`
 * @returns {object} Collection data if successful, or an error object.
 */
export async function get_yourCollectionEndpoint(request) {
	const response = { headers: { 'Content-Type': 'application/json' } };

	const TYPE_ARTICLES = 'YOUR-ARTICLES-TYPE';
	const TYPE_ARTICLES_CATEGORIES = 'YOUR-ARTICLES-CATEGORIES-TYPE';
	const ID_ARTICLES = 'YOUR-ARTICLES-COLLECTION-ID';
	const ID_ARTICLES_CATEGORIES = 'YOUR-ARTICLES-CATEGORIES-COLLECTION-ID';

	const requestedType = request.query.coll;

	let collectionId = '';

	if (!requestedType) {
		response.body = { error: 'Missing collection ID parameter.' };
		return badRequest(response);
	}

	if (requestedType === TYPE_ARTICLES) {
		collectionId = ID_ARTICLES;
	} else if (requestedType === TYPE_ARTICLES_CATEGORIES) {
		collectionId = ID_ARTICLES_CATEGORIES;
	} else {
		// Handle cases where an unknown ID is passed
		response.body = { error: 'Invalid collection type.' };
		return badRequest(response);
	}

	try {
		const actualToken = validateAuthorizationHeader(
			request,
			ENDPOINT_FIND_COLLECTION
		);

		const decodedJwt = await decodeJwtToken(
			actualToken,
			WIX_AUTH_SECRET,
			EXPECTED_JWT_SUB_COLLECTION,
			ENDPOINT_FIND_COLLECTION
		);

		console.log('DEBUG: Actual Token: ', actualToken);
		console.log('DEBUG: Decoded JWT: ', decodedJwt);

		if (!decodedJwt) {
			console.error(
				`❌ [${ENDPOINT_FIND_COLLECTION}]: Invalid or missing JWT.`
			);
			response.body = { error: 'Unauthorized: Invalid token.' };
			return badRequest(response);
		}

		const collectionResult = await yourFindCollectionServiceFunction(
			collectionId
		);

		console.log(
			`🌐 [${ENDPOINT_FIND_COLLECTION}]: Received collection items: `,
			collectionResult.length ?? 0
		);

		response.body = collectionResult;
		return ok(response);
	} catch (error) {
		console.error(
			`❌ [${ENDPOINT_FIND_COLLECTION}]: Unexpected error caught: `,
			error
		);
		response.body = { error: error?.message || String(error) };
		return badRequest(response);
	}
}

/**
 * HTTP Function: get_yourMembersEndpoint
 * Endpoint: https://www.kiutarakbol.hu/_functions/yourMembersEndpoint
 *
 * @accepts GET with JSON body:
 * @requires Authorization header: `Bearer YOUR_JWT_TOKEN`
 * @returns {object} Members data if successful, or an error object.
 */
export async function get_yourMembersEndpoint(request) {
	const response = { headers: { 'Content-Type': 'application/json' } };

	try {
		const actualToken = validateAuthorizationHeader(
			request,
			ENDPOINT_FIND_MEMBERS
		);

		const decodedJwt = await decodeJwtToken(
			actualToken,
			WIX_AUTH_SECRET,
			EXPECTED_JWT_SUB_MEMBERS,
			ENDPOINT_FIND_MEMBERS
		);

		console.log('DEBUG: Actual Token: ', actualToken);
		console.log('DEBUG: Decoded JWT: ', decodedJwt);

		if (!decodedJwt) {
			console.error(`❌ [${ENDPOINT_FIND_MEMBERS}]: Invalid or missing JWT.`);
			response.body = { error: 'Unauthorized: Invalid token.' };
			return badRequest(response);
		}

		const membersResult = await yourFindMembersServiceFunction();

		console.log(
			`🌐 [${ENDPOINT_FIND_MEMBERS}]: Received number of members: `,
			membersResult.length ?? 0
		);

		response.body = membersResult;
		return ok(response);
	} catch (error) {
		console.error(
			`❌ [${ENDPOINT_FIND_MEMBERS}]: Unexpected error caught: `,
			error
		);
		response.body = { error: error?.message || String(error) };
		return badRequest(response);
	}
}
