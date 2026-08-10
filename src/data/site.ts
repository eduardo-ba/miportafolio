import type { TranslationKey } from "../i18n";

export const email = "leduardobarron@gmail.com";
export const phone = "+52 669 329 2473";
export const location = "Mazatlán, MX";

export const social = {
	github: "https://github.com/eduardo-ba",
	linkedin: "https://www.linkedin.com/in/luis-eduardo-barron-alvarez-60082b387/",
} as const;

export const cvPath = "/cv-luis-eduardo-barron.pdf";

export interface Project {
	titleKey: TranslationKey;
	eyebrowKey: TranslationKey;
	descKey: TranslationKey;
	noteKey: TranslationKey;
	techKey: TranslationKey;
	repo: string;
	year: string;
	featured?: boolean;
	mood: "lime" | "coral" | "blue" | "sand";
}

export const projects: Project[] = [
	{
		titleKey: "p1_title",
		eyebrowKey: "p1_eyebrow",
		descKey: "p1_desc",
		noteKey: "p1_note",
		techKey: "p1_tech_list",
		repo: "https://github.com/eduardo-ba/Pagina_Web_FrankOcean",
		year: "2026",
		featured: true,
		mood: "lime",
	},
	{
		titleKey: "p2_title",
		eyebrowKey: "p2_eyebrow",
		descKey: "p2_desc",
		noteKey: "p2_note",
		techKey: "p2_tech_list",
		repo: "https://github.com/eduardo-ba/miportafolio",
		year: "2026",
		featured: true,
		mood: "coral",
	},
	{
		titleKey: "p3_title",
		eyebrowKey: "p3_eyebrow",
		descKey: "p3_desc",
		noteKey: "p3_note",
		techKey: "p3_tech_list",
		repo: "https://github.com/eduardo-ba/sitio-web-responsivo",
		year: "2025",
		mood: "blue",
	},
	{
		titleKey: "p4_title",
		eyebrowKey: "p4_eyebrow",
		descKey: "p4_desc",
		noteKey: "p4_note",
		techKey: "p4_tech_list",
		repo: "https://github.com/eduardo-ba/red-CETIS127",
		year: "2024",
		mood: "sand",
	},
];

export interface SkillGroup {
	titleKey: TranslationKey;
	index: string;
	items: string[];
}

export const skills: SkillGroup[] = [
	{
		titleKey: "skills_front_title",
		index: "01",
		items: ["TypeScript", "JavaScript", "HTML", "CSS", "Responsive UI", "Accessibility"],
	},
	{
		titleKey: "skills_frameworks_title",
		index: "02",
		items: ["Astro", "React", "Node.js", "Vite", "SEO técnico"],
	},
	{
		titleKey: "skills_data_title",
		index: "03",
		items: ["MySQL", "SQLite", "Firebase", "Python", "Java"],
	},
	{
		titleKey: "skills_workflow_title",
		index: "04",
		items: ["Git", "GitHub", "Linux", "VS Code", "Redes & servidores"],
	},
];

export interface Capability {
	titleKey: TranslationKey;
	descKey: TranslationKey;
}

export const capabilities: Capability[] = [
	{ titleKey: "cap_1_title", descKey: "cap_1_desc" },
	{ titleKey: "cap_2_title", descKey: "cap_2_desc" },
	{ titleKey: "cap_3_title", descKey: "cap_3_desc" },
];

export interface Certification {
	labelKey: TranslationKey;
	url: string;
	issuer: "Cisco Networking Academy" | "Capacítate para el Empleo";
}

export const certifications: Certification[] = [
	{
		labelKey: "cert_ccna_srwe",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/certificates/?issuanceId=a9c7ddd7-4098-4be4-a2b0-e318a508dbfd",
	},
	{
		labelKey: "cert_ccna_itn",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/es/certificates?issuanceId=6124782b-c283-44a3-bdda-66d200ac890b",
	},
	{
		labelKey: "cert_net_basics",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/es/certificates?issuanceId=f88efae3-44d1-4b58-9697-d2402b0293ca",
	},
	{
		labelKey: "cert_linux",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/es/certificates?issuanceId=2fbc2b89-6d3f-4410-88c4-f23aee7c4dc2",
	},
	{
		labelKey: "cert_server_admin",
		issuer: "Capacítate para el Empleo",
		url: "https://capacitateparaelempleo.org/verifica/c0dc2a1a-48ff-4f41-bbba-fa27d0166de7/36dbbe32-abce-4f55-8330-b4a819841fc5",
	},
	{
		labelKey: "cert_cabling",
		issuer: "Capacítate para el Empleo",
		url: "https://capacitateparaelempleo.org/verifica/c0dc2a1a-48ff-4f41-bbba-fa27d0166de7/0832df80-f62a-46bb-b47a-fc5ebbdad964",
	},
];
